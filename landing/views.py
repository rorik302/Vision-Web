from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

from landing.forms import ContactForm
from landing.models import Landing


class LandingView(View):
    def get(self, request):
        form = ContactForm()

        landing = Landing.objects.prefetch_related('row_blocks_1', 'row_blocks_2', 'column_blocks').first()

        content = ''

        for block in landing.row_blocks_1.all():
            content += block.template

        for block in landing.row_blocks_2.all():
            content += block.template

        for block in landing.column_blocks.all():
            content += block.template

        content += render_to_string('landing/contact_form.html', {'form': form})

        context = {
            'title': landing.page_title,
            'header': landing.header.template,
            'content': content,
        }

        return render(request, 'landing/index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
                subject='Сообщение от пользователя',
                message=form.cleaned_data['text'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.EMAIL_HOST_USER]
            )
            return JsonResponse({'success': True})

        return JsonResponse({'success': False})

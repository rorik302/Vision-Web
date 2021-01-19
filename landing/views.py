from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

from landing.forms import ContactForm
from landing.services import get_landing
from landing.utils import generate_content


class LandingView(View):

    @staticmethod
    def get(request):
        landing = get_landing()

        content = generate_content([
            landing.rowblock1_set.all(),
            landing.rowblock2_set.all(),
            landing.columnblock_set.all()
        ])

        form = ContactForm()
        form_template = render_to_string('landing/contact_form.html', {'form': form})

        context = {
            'title': landing.page_title,
            'header': landing.header.template if landing.header else None,
            'content': content,
            'form': form_template
        }

        return render(request, 'landing/index.html', context)

    @staticmethod
    def post(request):
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

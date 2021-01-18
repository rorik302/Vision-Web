from django.shortcuts import render
from django.views import View

from landing.models import Landing


class LandingView(View):
    def get(self, request):
        landing = Landing.objects.prefetch_related('row_blocks_1', 'row_blocks_2', 'column_blocks').first()

        content = ''

        for block in landing.row_blocks_1.all():
            content += block.template

        for block in landing.row_blocks_2.all():
            content += block.template

        for block in landing.column_blocks.all():
            content += block.template

        context = {
            'title': landing.page_title,
            'header': landing.header.template,
            'content': content
        }

        return render(request, 'landing/index.html', context)

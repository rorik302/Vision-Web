from django.contrib import admin

from landing.admin.inlines import RowBlock1Inline, RowBlock2Inline, ColumnBlockInline
from landing.models.landing_models import Landing


class LandingAdmin(admin.ModelAdmin):
    inlines = [RowBlock1Inline, RowBlock2Inline, ColumnBlockInline]


admin.site.register(Landing, LandingAdmin)

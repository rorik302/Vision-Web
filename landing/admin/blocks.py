from django.contrib import admin

from landing.admin.inlines import CardInline, ParagraphInline, PercentInline, BenefitInline
from landing.models.block_models import ColumnBlock, RowBlock1, RowBlock2


class ColumnBlockAdmin(admin.ModelAdmin):
    inlines = [CardInline]


class RowBlock1Admin(admin.ModelAdmin):
    inlines = [ParagraphInline, PercentInline]


class RowBlock2Admin(admin.ModelAdmin):
    inlines = [BenefitInline]


admin.site.register(ColumnBlock, ColumnBlockAdmin)
admin.site.register(RowBlock1, RowBlock1Admin)
admin.site.register(RowBlock2, RowBlock2Admin)

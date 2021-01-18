from django.contrib import admin

from landing.models import Landing, Header, RowBlock_2, ColumnBlock, RowBlock_1


class BaseStackedInline(admin.StackedInline):
    extra = 0
    show_change_link = True


class RowBlock1Inline(BaseStackedInline):
    model = Landing.row_blocks_1.through


class RowBlock2Inline(BaseStackedInline):
    model = Landing.row_blocks_2.through


class ColumnBlockInline(BaseStackedInline):
    model = Landing.column_blocks.through


class LandingAdmin(admin.ModelAdmin):
    pass


class HeaderAdmin(admin.ModelAdmin):
    pass


class RowBlock1Admin(admin.ModelAdmin):
    pass


class RowBlock2Admin(admin.ModelAdmin):
    pass


class ColumnBlockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Landing, LandingAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(RowBlock_1, RowBlock1Admin)
admin.site.register(RowBlock_2, RowBlock2Admin)
admin.site.register(ColumnBlock, ColumnBlockAdmin)

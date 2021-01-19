from django.contrib import admin

from landing.models import Landing, Header, RowBlock2, ColumnBlock, RowBlock1, Navbar, NavbarMenu, NavbarMenuItem, \
    Hero, Percent, Paragraph, NavbarContact, Benefit, Card


class BaseInline(admin.TabularInline):
    extra = 0
    show_change_link = True


class MenuItemInline(BaseInline):
    model = NavbarMenuItem


class RowBlock1Inline(BaseInline):
    model = RowBlock1


class RowBlock2Inline(BaseInline):
    model = RowBlock2


class ColumnBlockInline(BaseInline):
    model = ColumnBlock


class ParagraphInline(BaseInline):
    model = Paragraph


class PercentInline(BaseInline):
    model = Percent


class BenefitInline(BaseInline):
    model = Benefit


class CardInline(BaseInline):
    model = Card


class LandingAdmin(admin.ModelAdmin):
    inlines = [RowBlock1Inline, RowBlock2Inline, ColumnBlockInline]


class HeaderAdmin(admin.ModelAdmin):
    pass


class RowBlock1Admin(admin.ModelAdmin):
    inlines = [ParagraphInline, PercentInline]


class RowBlock2Admin(admin.ModelAdmin):
    inlines = [BenefitInline]


class BenefitAdmin(admin.ModelAdmin):
    pass


class ColumnBlockAdmin(admin.ModelAdmin):
    inlines = [CardInline]


class CardAdmin(admin.ModelAdmin):
    pass


class NavbarAdmin(admin.ModelAdmin):
    pass


class NavbarMenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    exclude = ('items',)


class NavbarMenuItemAdmin(admin.ModelAdmin):
    pass


class HeroAdmin(admin.ModelAdmin):
    pass


class NavbarContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Landing, LandingAdmin)
admin.site.register(RowBlock1, RowBlock1Admin)
admin.site.register(RowBlock2, RowBlock2Admin)
admin.site.register(ColumnBlock, ColumnBlockAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(NavbarMenu, NavbarMenuAdmin)
admin.site.register(NavbarMenuItem, NavbarMenuItemAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(NavbarContact, NavbarContactAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Card, CardAdmin)

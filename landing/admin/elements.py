from django.contrib import admin

from landing.admin.inlines import MenuItemInline
from landing.models.element_models import Header, Benefit, Card, Navbar, NavbarMenu, NavbarMenuItem, Hero, NavbarContact


class BenefitAdmin(admin.ModelAdmin):
    pass


class CardAdmin(admin.ModelAdmin):
    pass


class HeaderAdmin(admin.ModelAdmin):
    pass


class HeroAdmin(admin.ModelAdmin):
    pass


class NavbarAdmin(admin.ModelAdmin):
    pass


class NavbarMenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    exclude = ('items',)


class NavbarMenuItemAdmin(admin.ModelAdmin):
    pass


class NavbarContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(NavbarMenu, NavbarMenuAdmin)
admin.site.register(NavbarMenuItem, NavbarMenuItemAdmin)
admin.site.register(NavbarContact, NavbarContactAdmin)

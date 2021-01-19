from django.db import models
from django.template.loader import render_to_string

from landing.models.block_models import RowBlock2, ColumnBlock, RowBlock1
from landing.models.mixins import TemplateMixin


class Benefit(TemplateMixin):
    image = models.ImageField(upload_to='img')
    text = models.CharField(max_length=200)
    block = models.ForeignKey(RowBlock2, on_delete=models.CASCADE)
    template_path = 'landing/benefit.html'

    class Meta:
        db_table = 'benefits'

    def __str__(self):
        return self.text


class Card(TemplateMixin):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    footer = models.CharField(max_length=100)
    background = models.CharField(max_length=30, null=True, blank=True, choices=(
        ('', ''), ('bg-blue', 'blue'), ('bg-purple-gradient', 'purple-gradient'), ('bg-marina', 'marina')
    ))
    block = models.ForeignKey(ColumnBlock, on_delete=models.CASCADE)
    template_path = 'landing/card.html'

    class Meta:
        db_table = 'cards'


class Header(TemplateMixin):
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE)
    hero = models.ForeignKey('Hero', on_delete=models.CASCADE)
    background_img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'headers'

    def __str__(self):
        return self.hero.text

    @property
    def template(self):
        context = {
            'navbar': self.navbar.template,
            'hero': self.hero.template
        }
        return render_to_string('landing/header.html', context)


class Hero(TemplateMixin):
    image = models.ImageField(upload_to='img')
    text = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)
    template_path = 'landing/hero.html'

    class Meta:
        db_table = 'heros'

    def __str__(self):
        return f'Hero {self.text}'


class Navbar(TemplateMixin):
    logo = models.ImageField(upload_to='img')
    menu = models.ForeignKey('NavbarMenu', on_delete=models.CASCADE)
    contact = models.ForeignKey('NavbarContact', on_delete=models.CASCADE)

    class Meta:
        db_table = 'navbars'

    def __str__(self):
        return 'Навигационная панель'

    @property
    def template(self):
        context = {
            'logo': self.logo,
            'menu': self.menu.template,
            'contact': self.contact.template
        }
        return render_to_string('landing/navbar.html', context)


class NavbarContact(TemplateMixin):
    text = models.CharField(max_length=50)
    template_path = 'landing/navbar_contact.html'

    class Meta:
        db_table = 'navbar_contacts'

    def __str__(self):
        return self.text


class NavbarMenu(TemplateMixin):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'navbar_menus'

    def __str__(self):
        return f'Меню {self.name}'

    @property
    def template(self):
        context = {
            'items': self.navbarmenuitem_set.all()
        }
        return render_to_string('landing/navbar_menu.html', context)


class NavbarMenuItem(TemplateMixin):
    text = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    menu = models.ForeignKey(NavbarMenu, on_delete=models.CASCADE)
    template_path = 'landing/navbar_menu_item.html'

    class Meta:
        db_table = 'navbar_menu_items'


class Paragraph(TemplateMixin):
    text = models.TextField(max_length=200)
    block = models.ForeignKey(RowBlock1, on_delete=models.CASCADE)
    template_path = 'landing/paragraph.html'

    class Meta:
        db_table = 'paragraphs'

    def __str__(self):
        return self.text[:50]


class Percent(TemplateMixin):
    number = models.IntegerField()
    text = models.CharField(max_length=100)
    block = models.ForeignKey(RowBlock1, on_delete=models.CASCADE)
    template_path = 'landing/percent.html'

    class Meta:
        db_table = 'percents'

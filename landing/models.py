from django.db import models
from django.template.loader import render_to_string


class Landing(models.Model):
    page_title = models.CharField(max_length=70)
    header = models.ForeignKey('Header', on_delete=models.CASCADE)

    def __str__(self):
        return self.page_title


class Header(models.Model):
    navbar = models.ForeignKey('Navbar', on_delete=models.CASCADE)
    hero = models.ForeignKey('Hero', on_delete=models.CASCADE)
    background_img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.hero.text

    @property
    def template(self):
        context = {
            'navbar': self.navbar.template,
            'hero': self.hero.template
        }
        return render_to_string('landing/header.html', context)


class Navbar(models.Model):
    logo = models.ImageField(upload_to='img')
    menu = models.ForeignKey('NavbarMenu', on_delete=models.CASCADE)
    contact = models.ForeignKey('NavbarContact', on_delete=models.CASCADE)

    def __str__(self):
        return 'Навигационная панель'

    @property
    def template(self):
        context = {
            'logo': self.logo.url,
            'menu': self.menu.template,
            'contact': self.contact.template
        }
        return render_to_string('landing/navbar.html', context)


class NavbarMenu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Меню {self.name}'

    @property
    def template(self):
        context = {
            'items': self.navbarmenuitem_set.all()
        }
        return render_to_string('landing/navbar_menu.html', context)


class NavbarMenuItem(models.Model):
    text = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    menu = models.ForeignKey(NavbarMenu, on_delete=models.CASCADE)

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/navbar_menu_item.html', context)


class Hero(models.Model):
    image = models.ImageField(upload_to='img')
    text = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)

    def __str__(self):
        return f'Hero {self.text}'

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/hero.html', context)


class NavbarContact(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/navbar_contact.html', context)


class RowBlock1(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey(Landing, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Row_Block_1'
        verbose_name_plural = 'Row_Blocks_1'

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {
            'title': self.title,
            'paragraphs': self.paragraph_set.all(),
            'percents': self.percent_set.all()
        }
        return render_to_string('landing/row_block_1.html', context)


class Paragraph(models.Model):
    text = models.TextField(max_length=200)
    block = models.ForeignKey(RowBlock1, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/paragraph.html', context)


class Percent(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=100)
    block = models.ForeignKey(RowBlock1, on_delete=models.CASCADE)

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/percent.html', context)


class RowBlock2(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey(Landing, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Row_Block_2'
        verbose_name_plural = 'Row_Blocks_2'

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {
            'title': self.title,
            'benefits': self.benefit_set.all()
        }
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/row_block_2.html', context)


class Benefit(models.Model):
    image = models.ImageField(upload_to='img')
    text = models.CharField(max_length=200)
    block = models.ForeignKey(RowBlock2, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/benefit.html', context)


class ColumnBlock(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey(Landing, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {
            'title': self.title,
            'cards': self.card_set.all()
        }
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/column_block.html', context)


class Card(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    footer = models.CharField(max_length=100)
    background = models.CharField(max_length=30, null=True, blank=True, choices=(
        ('', ''), ('bg-blue', 'blue'), ('bg-purple-gradient', 'purple-gradient'), ('bg-marina', 'marina')
    ))
    block = models.ForeignKey(ColumnBlock, on_delete=models.CASCADE)

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/card.html', context)

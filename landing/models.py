from django.db import models
from django.template.loader import render_to_string


class Landing(models.Model):
    page_title = models.CharField(max_length=70)
    header = models.ForeignKey('Header', on_delete=models.CASCADE)
    row_blocks_1 = models.ManyToManyField('RowBlock_1')
    row_blocks_2 = models.ManyToManyField('RowBlock_2')
    column_blocks = models.ManyToManyField('ColumnBlock')

    def __str__(self):
        return self.page_title


class Header(models.Model):
    logo = models.ImageField(upload_to='img')
    title = models.CharField(max_length=200)
    hero_img = models.ImageField(upload_to='img')
    background_img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/header.html', context)


class RowBlock_1(models.Model):
    title = models.CharField(max_length=100)
    text_1 = models.CharField(max_length=250, blank=True, null=True)
    text_2 = models.CharField(max_length=250, blank=True, null=True)
    percent_1 = models.CharField(max_length=3)
    percent_1_text = models.CharField(max_length=50, blank=True, null=True)
    percent_2 = models.CharField(max_length=3)
    percent_2_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Row_Block_1'
        verbose_name_plural = 'Row_Blocks_1'

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/row_block_1.html', context)


class RowBlock_2(models.Model):
    title = models.CharField(max_length=100)
    block_1_img = models.ImageField(upload_to='img')
    block_1_text = models.CharField(max_length=100, blank=True, null=True)
    block_2_img = models.ImageField(upload_to='img')
    block_2_text = models.CharField(max_length=100, blank=True, null=True)
    block_3_img = models.ImageField(upload_to='img')
    block_3_text = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Row_Block_2'
        verbose_name_plural = 'Row_Blocks_2'

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/row_block_2.html', context)


class ColumnBlock(models.Model):
    title = models.CharField(max_length=100)
    card_1_title = models.CharField(max_length=100, null=True, blank=True)
    card_1_text = models.CharField(max_length=200, null=True, blank=True)
    card_1_footer = models.CharField(max_length=100, null=True, blank=True)
    card_1_img = models.ImageField(upload_to='img', null=True, blank=True)
    card_2_title = models.CharField(max_length=100, null=True, blank=True)
    card_2_text = models.CharField(max_length=200, null=True, blank=True)
    card_2_footer = models.CharField(max_length=100, null=True, blank=True)
    card_2_img = models.ImageField(upload_to='img', null=True, blank=True)
    card_3_title = models.CharField(max_length=100, null=True, blank=True)
    card_3_text = models.CharField(max_length=200, null=True, blank=True)
    card_3_footer = models.CharField(max_length=100, null=True, blank=True)
    card_3_img = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string('landing/column_block.html', context)

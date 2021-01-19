from django.db import models
from django.template.loader import render_to_string


class ColumnBlock(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey('landing.Landing', on_delete=models.CASCADE)

    class Meta:
        db_table = 'column_blocks'
        verbose_name = 'Column_block'
        verbose_name_plural = 'Column_blocks'

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


class RowBlock1(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey('landing.Landing', on_delete=models.CASCADE)

    class Meta:
        db_table = 'row_blocks_1'
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


class RowBlock2(models.Model):
    title = models.CharField(max_length=100)
    landing = models.ForeignKey('landing.Landing', on_delete=models.CASCADE)

    class Meta:
        db_table = 'row_blocks_2'
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

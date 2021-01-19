from django.db import models

from landing.models.element_models import Header


class Landing(models.Model):
    page_title = models.CharField(max_length=70)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'landings'

    def __str__(self):
        return self.page_title

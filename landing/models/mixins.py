from django.db import models
from django.template.loader import render_to_string


class TemplateMixin(models.Model):
    template_path = None

    @property
    def template(self):
        context = {}
        for field in self._meta.fields:
            context[field.name] = field.value_from_object(self)
        return render_to_string(self.template_path, context)

    class Meta:
        abstract = True

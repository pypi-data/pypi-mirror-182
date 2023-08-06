
from django.db import models
from django.utils.translation import gettext as _

class DjangoDBCounterBase(models.Model):
    default_key = "default"

    key = models.CharField(max_length=128, db_index=True, verbose_name=_("Django DB Counter Key"))
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=_("Add Time"))
    mod_time = models.DateTimeField(auto_now=True, verbose_name=_("Modify Time"))

    class Meta:
        abstract = True

    @classmethod
    def get_next(cls, key=None):
        key = key or cls.default_key
        item = cls(key=key)
        item.save()
        return cls.objects.filter(pk__lte=item.pk).count()

class DjangoDBCounter(DjangoDBCounterBase):

    class Meta:
        verbose_name = _("Django DB Counter Record")
        verbose_name_plural = _("Django DB Counter Records")


from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DjangoDbCounterConfig(AppConfig):
    name = 'django_db_counter'
    verbose_name = _("Django DB Counter")
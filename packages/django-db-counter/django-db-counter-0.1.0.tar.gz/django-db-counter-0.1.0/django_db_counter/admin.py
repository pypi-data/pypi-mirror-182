from django.contrib import admin

from .models import DjangoDBCounter


class DjangoDBCounterAdmin(admin.ModelAdmin):
    list_display = ["pk", "key", "add_time", "mod_time"]
    list_filter = ["key"]


admin.site.register(DjangoDBCounter, DjangoDBCounterAdmin)

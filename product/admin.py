from django.contrib import admin

# Register your models here.

from .models import MonitorFlat, MonitorCRT, MonitorModel

admin.site.register(MonitorFlat)
admin.site.register(MonitorCRT)
# admin.site.register(MLClass)
# admin.site.register(Attribute)

class PersonAdmin(admin.ModelAdmin):
    pass
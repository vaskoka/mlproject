from django.contrib import admin

# Register your models here.

from .models import MonitorFlat, MonitorCRT, MonitorModel, MLClass, Attribute

admin.site.register(MonitorFlat)
admin.site.register(MonitorCRT)
# admin.site.register(MLClass)
# admin.site.register(Attribute)
@admin.register(MLClass, Attribute)
class PersonAdmin(admin.ModelAdmin):
    pass
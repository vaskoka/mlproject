from django.contrib import admin

# Register your models here.
from .models import MLClass, Attribute

admin.site.register(MLClass)
admin.site.register(Attribute)
from django.contrib import admin

# Register your models here.
from .models import Clabject, Attribute


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Clabject')

admin.site.register(Clabject)



admin.site.register(Attribute)
from django.contrib import admin

# Register your models here.
from .models import  Clabject, Attribute, MLDiagram

#admin.site.register(Clabject)
#admin.site.register(Attribute)
admin.site.register(MLDiagram)


class AttributeInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Attribute

# Define the admin class
class ClabjectAdmin(admin.ModelAdmin):
    list_display = ('name','potency','subclassOf','instanceOf')
    inlines = [AttributeInline]

# Register the admin class with the associated model
admin.site.register(Clabject, ClabjectAdmin)


# Register the Admin classes for Attribute using the decorator
@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name','potency', 'clabject')

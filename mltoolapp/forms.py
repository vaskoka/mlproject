
from tkinter.tix import Form
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django import forms

from mltoolapp.models import Attribute, Clabject


class InstantiateClabjectForm(forms.Form):
       name = forms.CharField(max_length=100, required=True)
       potency = forms.IntegerField(min_value=0 )
       attr_value = forms.CharField()

    
# creating a form
class CreateClabject(forms.ModelForm):
       class Meta:
              model = Clabject
              fields = [
                  'name',
                  'potency',
                  'mldiagram',
                  'subclassOf',
                  'instanceOf',
                  ]
             
# Form for the create attribute function view      
class CreateAttribute(forms.ModelForm):
       class Meta:
              model = Attribute
              fields = [
                  'name',
                  'potency',
                  'data_type',
                  'clabject',
                  'value',
                  ]
             
       

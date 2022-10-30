from tkinter.tix import Form
from django.forms import ValidationError
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django import forms
from django.utils.translation import gettext_lazy as _
from mltoolapp.models import Attribute, Clabject


class InstantiateClabjectAttributeForm(forms.ModelForm):
       class Meta:
              model = Attribute
              fields = '__all__'

class InstantiateClabjectForm(forms.ModelForm):
       class Meta:
              model = Clabject
              fields = '__all__'
       

    
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
       def clean(self):
              cleaned_data = super().clean()
              value = cleaned_data.get("value")
              potency = cleaned_data.get("potency")
              
                     
              if value is None and potency == 0:
                     raise ValidationError( {'value': _('The Potency is 0 and this attribute needs a value, Please add a value!')} )
                            
                            
       

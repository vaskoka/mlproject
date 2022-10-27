
from django import forms

from mltoolapp.models import Attribute, Clabject


class InstantiateClabjectForm(forms.Form):
       name = forms.CharField(max_length=100, required=False)
       potency = forms.IntegerField()
       
       
      
              
            
   

from django import forms

from mltoolapp.models import Attribute, Clabject


class InstantiateClabjectForm(forms.Form):
       model = Attribute
       name = forms.CharField(max_length=100, required=True)
       potency = forms.IntegerField(min_value=0, )
       
       
      
              
            
   
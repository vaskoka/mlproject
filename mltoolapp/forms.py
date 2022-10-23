from django import forms

from mltoolapp.models import Clabject


class InstantiateClabjectForm(forms.Form):
       name = forms.CharField(max_length=100)
    
             
              
              
              
            
   
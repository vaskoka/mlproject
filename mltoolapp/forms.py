
from django import forms

from mltoolapp.models import Clabject


class InstantiateClabjectForm(forms.Form):
       name = forms.CharField(max_length=100, required=False)
       potency = forms.IntegerField()
      #  class Meta:
      #         model = Clabject
      #         fields = '__all__'
             
     
              
            
   
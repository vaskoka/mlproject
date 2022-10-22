from django import forms

class InstantiateClabject(forms.Form):
   name = forms.CharField(max_length=255, required=True)
   potency = forms.CharField(max_length=255, required=True)
   subclassOf = forms.CharField(required=True)
   instanceOf = forms.CharField()
   
from enum import unique
from random import choices
from django.urls import reverse
from django.db import models

# Create your models here.

class MLDiagram(models.Model):
    name = models.CharField(max_length=255, unique=True)
  
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('mldiagram-detail',  args=[str(self.id)])

class Clabject(models.Model):
    name = models.CharField(max_length=255)
    potency = models.CharField(max_length=255)
    subclassOf = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subclass',default='None')
    instanceOf = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='instance', default='None')
    mldiagram = models.ForeignKey (MLDiagram, on_delete=models.CASCADE, related_name='mldiagram')
  
    
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('clabject-detail', args=[str(self.id)])
            
       
    
    
class Attribute(models.Model):
    DATA_TYPE = (
        ('STRING', 'Text input'),
        ('INT','Number input'),
        ('DOUBLE','Decimal number'),
        ('DATE', 'Date input'),
    )
    
    name = models.CharField(max_length=255)
    potency = models.CharField(max_length=255)
    data_type = models.CharField( max_length=255, choices=DATA_TYPE, help_text='Data type')
    clabject = models.ForeignKey(Clabject, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True, blank=True, default='null')
    
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    
    def display_attributes(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return self.clabject # .join([clabject for clabject in self.clabject.all()])

    display_attributes.short_description = 'Clabject'


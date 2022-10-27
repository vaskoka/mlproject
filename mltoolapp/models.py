from django.db.models import UniqueConstraint
from random import choices
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class MLDiagram(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True)
  
    def __str__(self):
        return self.name 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('mldiagram-detail',  args=[str(self.slug)])



class Clabject(models.Model):
    name = models.CharField(max_length=255)
    potency = models.PositiveSmallIntegerField()
    subclassOf = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subclass',default='None')
    instanceOf = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='instance', default='None')
    mldiagram = models.ForeignKey (MLDiagram, on_delete=models.CASCADE, related_name='mldiagram')
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name', 'mldiagram'],
                name='unique_clabject'),
        ]
  
    
    def __str__(self):
        return self.name 
        """__str__ _summary_
        """    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('clabject-detail', args=[str(self.id)])
        """get_absolute_url _summary_

        Returns:
            _type_: _description_
        """    
              
class Attribute(models.Model):
    DATA_TYPE = (
        ('STRING', 'Text input'),
        ('INT','Number input'),
        ('DOUBLE','Decimal number'),
        ('DATE', 'Date input'),
    )
    
    name = models.CharField(max_length=255)
    potency = models.PositiveSmallIntegerField()
    data_type = models.CharField( max_length=255, choices=DATA_TYPE, help_text='Data type')
    clabject = models.ForeignKey(Clabject, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True, blank=True, default='null')
    
   
    class Meta:
        ordering = ['name']
        constraints = [
            UniqueConstraint(
                fields=['name', 'clabject'],
                name='unique_attribute'),
            
        ]
            
    def __str__(self):
           return self.name
    
    def display_attributes(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return self.clabject # .join([clabject for clabject in self.clabject.all()])

    display_attributes.short_description = 'Clabject'
    
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('attribute-detail', args=[str(self.id)])


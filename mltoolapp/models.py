from django.db.models import UniqueConstraint
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class MLDiagram(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True)
  
    def __str__(self):
        return self.name 
    
    # creates a slug of the name fo URL (for examle Product diagram -> Product-diagram)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

    def get_absolute_url(self):
        """Returns the url to access a particular mldiagram instance."""
        return reverse('mldiagram-detail',  args=[str(self.slug)])



class Clabject(models.Model):
    name = models.CharField(max_length=255)
    potency = models.PositiveSmallIntegerField()
    subclassOf = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subclass',default='None')
    instanceOf = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='instance', default='None')
    mldiagram = models.ForeignKey (MLDiagram, on_delete=models.CASCADE, related_name='mldiagram')
    
    class Meta:
        constraints = [
            # Unique name within one mldiagram
            UniqueConstraint(
                fields=['name', 'mldiagram'],
                name='unique_clabject'),
        ]
  
    
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
    potency = models.PositiveSmallIntegerField()
    data_type = models.CharField( max_length=255, choices=DATA_TYPE, help_text='Data type')
    clabject = models.ForeignKey(Clabject, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True, blank=True, default='null')
    
   
    class Meta:
        ordering = ['name']
        constraints = [
            # Unique attribute name within one clabject
            UniqueConstraint(
                fields=['name', 'clabject'],
                name='unique_attribute'),
            
        ]
            
    def __str__(self):
           return self.name
    
    
    def get_absolute_url(self):
        """Returns the url to access a particular attribute instance."""
        return reverse('attribute-detail', args=[str(self.id)])


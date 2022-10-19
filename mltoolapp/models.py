from django.db import models

# Create your models here.



class Clabject(models.Model):
    name = models.CharField(max_length=255)
    potency = models.CharField(max_length=255)
    subclassOf = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subclass',default='None')
    instanceOf = models.ForeignKey('self', null=True,blank=True,on_delete=models.CASCADE, related_name='instance', default='None')
   # ml_project = models.ForeignKey(MLdesign, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 
    
class Attribute(models.Model):
    name = models.CharField(max_length=255)
    potency = models.CharField(max_length=255)
    data_type = models.CharField( max_length=255, default='Null')
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


# class ClabjectRlationship(models.Model):
  #  type = models.ManyToManyField('RelationshipType', blank=True,
   #                                related_name='clabject_relationships')
   # from_clabject = models.ForeignKey('Clabject', related_name='from_contacts', on_delete=models.CASCADE)
   # to_clabject = models.ForeignKey('Clabject', related_name='to_contacts', on_delete=models.CASCADE)

    #class Meta:
   #     unique_together = ('from_clabject', 'to_clabject')
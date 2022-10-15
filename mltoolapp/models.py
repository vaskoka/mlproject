from django.db import models

# Create your models here.
class Clabject(models.Model):
    name = models.CharField(max_length=255)
    clabject = models.OneToOneField('self', on_delete=models.CASCADE, null=True,blank=True, related_name='classobject', default='None')
    subclassOf = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subclass',default='None')
    instanceOf = models.ManyToManyField('self', null=True,blank=True, related_name='instance', default='None')
   
    def __str__(self):
        return self.name
    
class Attribute(models.Model):
    name = models.CharField(max_length=255)
    clabject = models.ForeignKey(Clabject, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# class ClabjectRlationship(models.Model):
  #  type = models.ManyToManyField('RelationshipType', blank=True,
   #                                related_name='clabject_relationships')
   # from_clabject = models.ForeignKey('Clabject', related_name='from_contacts', on_delete=models.CASCADE)
   # to_clabject = models.ForeignKey('Clabject', related_name='to_contacts', on_delete=models.CASCADE)

    #class Meta:
   #     unique_together = ('from_clabject', 'to_clabject')
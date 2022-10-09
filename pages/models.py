from django.db import models

# Create your models here.

class MLClass(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    
    
class Attribute(models.Model):
    mlclass = models.ForeignKey(MLClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dataType = models.CharField(max_length=50)
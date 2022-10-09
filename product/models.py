from django.db import models

# Create your models here.

# This is a test class added above after the model is created, once migrated it populated all the tables.
# It is important that the top-moast class inherit models.Model 
class MasterProduct(models.Model):
    master_pr = models.CharField(default='Test', max_length=100)
    
    class Meta():
        abstract = True
 
# The top class of the model - Meta abstraction        
class ProductType(MasterProduct):
    master_pr = models.CharField(default='Test1', max_length=100)
    name = models.CharField(max_length=200)
    class Meta():
       abstract = True
    
#  Computer branch  
class ComputerModel(ProductType):
    processor = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    class Meta():
        abstract = True
        
# name and processor ore overriden and a default value is assigned, every ComputerStandard 
# object will inherit these vaues 
class ComputerStandard(ComputerModel):
    name = models.CharField(max_length=255, default='PC Standard')
    processor = models.CharField(max_length=100, default='3.1 GHz')
    
class ComputerDeluxe(ComputerModel):
    name = models.CharField(max_length=255, default='PC Deluxe.')
    processor = models.CharField(max_length=100, default='4.5 GHz')
    
# Monitor branch
    
class MonitorModel(ProductType):
    size = models.CharField(max_length=50)
    picQty = models.IntegerField()
    class Meta():
        abstract = True
        
class MonitorFlat(MonitorModel):
    name = models.CharField(max_length=255, default='Flat 19')
    size = models.CharField(max_length=50, default='19')
    
class MonitorCRT(MonitorModel):
    name = models.CharField(max_length=255, default='CRT 21')
    size = models.CharField(max_length=50, default='21')
    
 # Multi-level classes    
    
class MLClass(models.Model):
    name = models.CharField(max_length=255)
    
    
    
class Attribute(models.Model):
    mlclass = models.ForeignKey(MLClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dataType = models.CharField(max_length=50)
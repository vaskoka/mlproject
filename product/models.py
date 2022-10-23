from django.db import models


# Create your models here.
 
# The top class of the model - Meta abstraction        
class ProductType(models.Model):
    PTname = models.CharField(max_length=200,verbose_name='name', default='')
   
#  Computer branch  
class ComputerModel(ProductType):
    CMprocessor = models.CharField(max_length=100,verbose_name='processor', default='')
    CMprice = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price', default='')
    
        
# name and processor ore overriden and a default value is assigned, every ComputerStandard 
# object will inherit these vaues 
class ComputerStandard(ComputerModel):
    CSname = models.CharField(max_length=255, default='PC Standard', verbose_name='name')
    CSprocessor = models.CharField(max_length=100, default='3.1 GHz', verbose_name='processor')
    
        
class ComputerDeluxe(ComputerModel):
    CDname = models.CharField(max_length=255, default='PC Deluxe.',verbose_name='name')
    CDprocessor = models.CharField(max_length=100, default='4.5 GHz',verbose_name='processor')
    
# Monitor branch
    
class MonitorModel(ProductType):
    MMsize = models.CharField(max_length=50,verbose_name='size', default='')
    MMpicQty = models.IntegerField(verbose_name='picQty', default='')
    
        
class MonitorFlat(MonitorModel):
    MMname = models.CharField(max_length=255, default='Flat 19', verbose_name='name')
    MFsize = models.CharField(max_length=50, default='19',verbose_name='size')
    
class MonitorCRT(MonitorModel):
    MCname = models.CharField(max_length=255, default='CRT 21',verbose_name='name')
    MCsize = models.CharField(max_length=50, default='21', verbose_name='name')
    
 # Multi-level classes    
 
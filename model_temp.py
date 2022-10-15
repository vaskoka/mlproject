from django.db import models 

class ProductType(models.Model):
	name = models.CharField(max_length=255)
	
	class Meta(): 
		abstract = True

class ComputerModel(ProductType):
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=9)
	
	class Meta(): 
		abstract = True

class MonitorModel(ProductType):
	size = models.CharField(max_length=255)
	picQlty = models.IntegerField()
	
	class Meta(): 
		abstract = True

class ComputerStandard(ComputerModel):
	name = models.CharField(max_length=255,default="PC standard")
	processor = models.CharField(max_length=255,default="3.1 GHz")
	price = models.DecimalField(decimal_places=2, max_digits=9)
	
class ComputerDeluxe(ComputerModel):
	name = models.CharField(max_length=255,default="PC deluxe")
	processor = models.CharField(max_length=255,default="4.5 GHz")
	price = models.DecimalField(decimal_places=2, max_digits=9)
	

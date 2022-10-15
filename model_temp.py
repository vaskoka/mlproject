class ProductType(models.Model):
	name = models.CharField(max_length=255)
	
class ComputerModel(models.Model):
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2)
	
class MonitorModel(models.Model):
	size = models.CharField(max_length=255)
	picQlty = models.IntegerField()
	
class ComputerStandard(models.Model):
	name = models.CharField(max_length=255)
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2)
	
class ComputerDeluxe(models.Model):
	name = models.CharField(max_length=255)
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2)
	
class C1(models.Model):
	name = models.CharField(max_length=255)
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2)
	
class C2(models.Model):
	name = models.CharField(max_length=255)
	processor = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2)
	

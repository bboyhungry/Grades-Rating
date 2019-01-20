from django.db import models

class Classes(models.Model):
	passRate = models.DecimalField(max_digits = 2,decimal_places = 2)
	failRate = models.DecimalField(max_digits = 2,decimal_places = 2)
	enrollment = models.BigIntegerField()

class Professor(models.Model):
	theClass = models.ForeignKey(Classes, on_delete = models.CASCADE)
	name = models.CharField(max_length = 250)
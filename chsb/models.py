from django.db import models
from django.contrib.auth.models import User
from pupils.models import Students

grad=[
	("501", 501),
	("502", 502),
	("503", 503),
	("601", 601),
	("602", 602),
	("603", 603),
	("701", 701),
	("702", 702),
	("703", 703),
	("801", 801),
	("802", 802),
	("803", 803),
	("901", 901),
	("902", 902),
	("903", 903),
	("1001", 1001),
	("1002", 1002),
	("1003", 1003),
	("11", 11)
]
class Chsblar(models.Model):
	time = models.DateField()
	coun = models.PositiveIntegerField()
	def __str__(self):
		return "ChSB" + f"-{self.coun}" + f"({self.time})"
class InnerChsb(models.Model):
	grupIn = models.ForeignKey(Chsblar, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	chsbCount = models.PositiveIntegerField()

	def __str__(self):
		return self.name + '-guruh' + " " +f"({self.chsbCount})"

class Marks(models.Model):
	GroupIn = models.ForeignKey(InnerChsb, on_delete=models.CASCADE )
	user = models.ForeignKey(Students, on_delete=models.CASCADE)
	grade = models.CharField(max_length=120, choices = grad)
	chsbCount = models.PositiveIntegerField()
	jamiBaho = models.FloatField()
	algebra = models.FloatField()
	english = models.FloatField()
	geometriya = models.FloatField(blank=True, null=True)
	fizika = models.FloatField(blank=True, null=True)
	
	
	def __str__(self):
		return self.user.full_name + " " + self.user.grade + f"({self.chsbCount})"

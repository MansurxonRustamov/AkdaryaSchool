from django.db import models
from django.contrib.auth.models import User
subject = [
	("Matematika", 'Matematika'),
	("Ingliz tili", 'Ingliz Tili'),
	("Fizika", 'Fizika'),
	("Ona tili va adabiyot", 'Ona tili va adabiyot'),
	("Tarix", 'Tarix'),
	("Huquq", 'Huquq'),

]
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
class ContactUs(models.Model):
	ism = models.CharField(max_length=120)
	telefon_raqam = models.BigIntegerField()
	xabar = models.TextField()
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.ism

class Teachers(models.Model):
	full_name = models.CharField(max_length=120)
	phone= models.BigIntegerField()
	age= models.PositiveIntegerField()
	subject = models.CharField(max_length=120, choices=subject)
	about = models.TextField()
	image=models.ImageField(upload_to='teacherimages/')

	def __str__(self):
		return self.full_name

class Yutuqlar(models.Model):
	image=models.ImageField(upload_to='yutuqlar/')
	about = models.TextField()
	name = models.CharField(max_length=120)
	typ = models.CharField(max_length=120)
	time = models.DateField()

	def __str__(self):
		return self.name

class Students(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=255)
	about = models.TextField()
	grade = models.CharField(max_length=120, choices=grad)
	image = models.ImageField(upload_to='pupils/')

	def __str__(self):
		return self.full_name + " " + self.grade

class Rooms(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(upload_to="rooms/")

	def __str__(self):
		return self.name
	




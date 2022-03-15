from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from datetime import datetime

class LastLogin(models.Model):
	id = models.SmallAutoField(primary_key=True)
	date = models.DateTimeField(default=timezone.now, editable=False)


class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
	first_name = models.CharField(max_length=50, null=False, blank=True)
	last_name = models.CharField(max_length=50, null=False, blank=True)
	classe = models.CharField(max_length=50, null=False, blank=True)
	date = models.DateTimeField(default=timezone.now)
	numero_matricule = models.BigIntegerField()

	def save(self, *args, **kwargs):
		if not self.numero_matricule :
			self.numero_matricule = self.generateMatricule()
		return super().save(*args, **kwargs)

	def generateMatricule(self):
		year = datetime.date.today().year
		return "{}{:0>2d}".format(year,'/', self.student_id.id)
	
	def fullname(self):
		return self.first_name+" "+self.last_name

	def __str__(self):
		return self.fullname
	
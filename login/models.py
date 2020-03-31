from django.db import models
# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=225)
	password=models.CharField(max_length=130)
	email	=models.EmailField(max_length=225)
	active	=models.BooleanField(default=True)
	favourites=models.CharField(max_length=800,default="")
	recents=models.CharField(max_length=800,default="")
	accesspin=models.IntegerField(default=-999)

	USERNAME_FIELD = "email"

	def __str__(self):
		return self.name

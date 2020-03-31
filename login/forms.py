from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields =['name','email','password1','password2']
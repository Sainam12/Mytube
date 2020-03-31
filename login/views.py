from django.shortcuts import render,redirect
import requests
import random
from passlib.hash import pbkdf2_sha256
from .models import User
from django.contrib import messages
from django.shortcuts import render,get_object_or_404

# Create your views here.
def login(request):
	user=User()
	err=""
	if request.method=='POST':
		name=request.POST['name']
		password=request.POST['password']
		user=authenticate(name,password)
		if user==None:
			err="invalid Username or Password"
		else:
			context={'user':user}
			user.accesspin=random.randrange(1000,9999)
			user.save()
			print()
			str1="/favourites/"+str(user.accesspin)
			print(str1)
			return redirect(str1)
	return render(request,'login/login.html',{'err':err})

def register(request):
	errs=[]
	if request.method =='POST':
		val=0
		name=request.POST['name']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']


		if User.objects.filter(name=name).exists():
			val+=1
			errs.append("Username taken")
		else:
			errs.append("")

		if User.objects.filter(email=email).exists():
			val+=1
			errs.append("Email taken")
		else:
			errs.append("")
		if password1 != password2 :
			val+=1
			errs.append("Enter same password in both fields")
		else:
			errs.append("")
		if val==0:
			password= pbkdf2_sha256.encrypt(password1,rounds=12000,salt_size=32)
			user= User.objects.create(name=name,password=password,email=email)
			user.save();
			return redirect('/user/login')
		context={'errs':errs}
		return render(request,'login/register.html',context)

	else:
		context={'errs':errs}
		return render(request,'login/register.html',context)
def authenticate(name,password):
	for user_object in User.objects.all():
			if user_object.name==name:
				print(pbkdf2_sha256.verify(password,user_object.password))
				return user_object
	return None

def logout(request,accesspin):
	user = get_object_or_404(User,accesspin=int(accesspin))
	user.accesspin=-999
	user.save()
	user=None
	return redirect('/favourites')
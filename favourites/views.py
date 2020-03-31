from django.shortcuts import render,redirect
import requests
from django.shortcuts import render,get_object_or_404
from login.models import User
# Create your views here.
def favourites(request):
	context={'user':None}
	return render(request,'favourites/favourites.html',context)

def lfavourites(request,accesspin):
	user = get_object_or_404(User,accesspin=int(accesspin))
	context={'user':user}
	return render(request,'favourites/favourites.html',context)


from django.urls import path
from . import views
urlpatterns = [
	path('',views.favourites,name='fav'),
	path('<accesspin>/',views.lfavourites,name='lfav'),
]
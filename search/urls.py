
from django.urls import path
from . import views
urlpatterns = [
	path('<accesspin>/',views.index,name='index'),
]

from django.urls import path
from . import views
urlpatterns = [
	path('',views.recents,name='rec'),
	path('<accesspin>/',views.lrecents,name='lrec')
]
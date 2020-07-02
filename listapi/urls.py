from django.urls import path
from . import views

urlpatterns = [
 	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('base/', views.base, name="base"),
	path('charts/', views.charts, name="charts"),
	path('youtube/', views.youtube, name="youtube"),
	path('learn/', views.learn, name="learn"),
	path('cards/', views.cards, name="cards")

]

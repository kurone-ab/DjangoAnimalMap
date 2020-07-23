from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('', views.home, name='home'),
    
]
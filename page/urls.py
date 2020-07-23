from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('', views.home, name='home'),
    path('save/', views.post_save, name='save'),
]

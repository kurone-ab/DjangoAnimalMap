from django.db import models


# Create your models here.
class Post(models.Model):
    lat = models.CharField(max_length=40)
    lng = models.CharField(max_length=40)
    cat_name = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    action = models.CharField(max_length=20)
    image = models.ImageField(blank=True)

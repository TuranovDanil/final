from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

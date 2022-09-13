import code
from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
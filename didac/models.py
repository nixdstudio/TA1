from django.db import models

# Create your models here.
class Cards(models.Model):
    name = models.CharField(max_length=50)
    ins = models.CharField(max_length=50)
    file = models.FileField(default=1)
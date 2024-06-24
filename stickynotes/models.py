from django.db import models


# Create your models here.
class Stickynote(models.Model):
    name = models.CharField(max_length=40)
    sets = models.SmallIntegerField()
    description = models.TextField()
    creator = models.CharField(max_length=30)

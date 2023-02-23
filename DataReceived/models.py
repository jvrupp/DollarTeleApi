from django.db import models

# Create your models here.

class DataBet(models.Model):
    digit = models.CharField(max_length=25)
    color=models.CharField(max_length=25)
    timestamp = models.IntegerField()


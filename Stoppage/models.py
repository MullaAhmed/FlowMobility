from sqlite3 import Timestamp
from django.db import models

from django.shortcuts import render,HttpResponse

# Create your models here.
class Acc_Data(models.Model):
    date=models.CharField("Todays Date",default="Today",max_length=20)
    timestamp=models.CharField("",default="LIN_ACC",max_length=100)
    sensor=models.CharField("Sensor Type",default="LIN_ACC",max_length=100)
    x=models.FloatField("X ACC")
    y=models.FloatField("Y ACC")
    z=models.FloatField("Z ACC")
    

    def __str__(self):
        return (self.date)

class Loc_Data(models.Model):
    date=models.CharField("Todays Date",default="Today",max_length=20)
    timestamp=models.CharField("",default="LIN_ACC",max_length=100)
    latitude=models.FloatField("Latitude")
    longitude=models.FloatField("Longitude")


    def __str__(self):
        return (self.date)

class Stop_Data(models.Model):
    latitude=models.FloatField("Latitude")
    longitude=models.FloatField("Longitude")


    def __str__(self):
        return (self.date)


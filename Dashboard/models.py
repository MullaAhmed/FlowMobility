from django.db import models
from datetime import date
from django.utils.timezone import datetime

# Create your models here.
class DashboardDayToDay(models.Model):
    username = models.CharField("Name",max_length=100)
    date=models.DateField("Todays Date",default=date.today())
    total_downloads=models.IntegerField("Total Downloads Till Date")
    total_drivers=models.IntegerField("Total Drivers as of Today")
    total_active_drivers=models.IntegerField("Total Active Drivers as of Today") 
    active_drivers_to_downloads=models.FloatField("Total Active Drivers/Downloads as of Today")
    total_trips=models.IntegerField("Total Trips Till Date")
    tota_distance=models.IntegerField("Total Distance Till Date")
    average_distance_per_trip=models.FloatField("Total Distance/Trips Till Today") 
    total_cashless_payments=models.IntegerField("Total Cashless Payments Till Date")
    total_cash_payments=models.IntegerField("Total Cash Payments (Trips-Cashless) Till Date")
    total_drivers_revenue=models.FloatField("Total Drivers Revenue Till Today") 
    total_meiro_revenue=models.FloatField("Total Merio Revenue Till Today") 

    def __str__(self):
        return (self.date)

class DashboardHourToHour(models.Model):
    #Starting time slot
    username = models.CharField("Name",max_length=100)
    date=models.DateField("Todays Date",default=date.today())
    hour_slot=models.CharField("Hour Slot (24Hours Format)",max_length=100)
    total_trips=models.IntegerField("Total Trips This hour")
    
    def __str__(self):
        return '%s - %s' %(self.date,self.hour_slot)

class DashboardTripToTrip(models.Model):
    username = models.CharField("Name",max_length=100)
    date=models.DateField("Todays Date",default=date.today())
    trip_id=models.CharField("Trip ID",max_length=100)
    trip_status=models.CharField("Trip Status",max_length=100)
    driver_id=models.CharField("Driver ID",max_length=100)
    driver_status=models.CharField("Driver Status",max_length=100)
   
    def __str__(self):
        return (self.trip_id)
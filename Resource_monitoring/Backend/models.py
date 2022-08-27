from pyexpat import model
from django.db import models
from datetime import time

# Create your models here.
class alerts(models.Model):
    id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey("session_data", verbose_name="Session_id", on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    temperature_in_range = models.BooleanField()
    humidity_in_range = models.BooleanField()
     
    class Meta:
        db_table = "Alerts"
    

class session_data(models.Model):
    session_ID = models.CharField(max_length=10,primary_key=True)
    numbers = models.IntegerField()
    serial = models.CharField(max_length=20)
    date = models.DateField(auto_now=False, auto_now_add=False)
    session_start_time = models.CharField(max_length= 15)
    session_end_time = models.CharField(max_length=15)
    session_status = models.BooleanField()
    temp_highest_level = models.FloatField()
    temp_lowest_level = models.FloatField()
    humidity_highest_level = models.FloatField()
    humidity_lowest_level = models.FloatField()
    time_interval = models.TimeField(default= time(0,15,0))

    class Meta:
        db_table = "Session_data"


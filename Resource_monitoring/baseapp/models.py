from pyexpat import model
from tokenize import group
from django.db import models
from datetime import time
from django.contrib.auth.models import User
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

class group_privileges(models.Model):
    user_access_control = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50,unique=True)
    print_report = models.BooleanField()
    view_time_table = models.BooleanField()
    view_channel_info = models.BooleanField()
    create_user = models.BooleanField()
    delete_user = models.BooleanField()
    create_grp = models.BooleanField()
    delete_grp = models.BooleanField()
    grp_list = models.BooleanField()
    add_session = models.BooleanField()
    delete_session = models.BooleanField()
    class Meta:
        db_table = "group_privileges"


class user_extra_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='userdetails')
    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)
    group_name = models.ForeignKey(group_privileges, on_delete=models.CASCADE, default=None, verbose_name='group_privileges')
    session_tokens =  models.CharField(max_length=50)
    class Meta:
        db_table = "user_extra_details"

class userlogs(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='userdetails')
    logs = models.CharField(max_length= 50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "userlogs"

class drug_template(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50, unique=True)
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    max_humidity = models.FloatField()
    min_humidity = models.FloatField()

    class Meta:
        db_table = "drug_template"

class probe(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.IntegerField()
    probe_offset = models.IntegerField()
    status = models.BooleanField()

    class Meta:
        db_table = "probe"

class device(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=30)
    baud_rate = models.IntegerField()
    parity_bit = models.BooleanField()
    stop_bit = models.BooleanField()

    class Meta:
        db_table = "device"


# class N_table(models.Model), {
#     id = models.AutoField(primary_key=True)
#     temperature = models.PositiveIntegerField(max_length=3)
#     humidity = models.PositiveIntegerField(max_length=3)
#     timestamp = models.DateTimeField(auto_now_add=True, unique=True)
# })

# timestamp timestamp , 
# CONSTRAINT unique_timestamp UNIQUE (timestamp) 

# Person = type('Person', (models.Model,), {
#     'first_name': models.CharField(max_length=255),
#     'last_name': models.CharField(max_length=255),
# })
# model = type(name, (models.Model,), attrs)


from datetime import datetime, time
import random
from django.shortcuts import render, redirect
from baseapp.models import session_data

# Create your views here.
def home(request):
    pass

def dashboard(request):
    return render(request,"Dashboard.html")

def addSession(request):
    random_number = random.randint(0,500)
    timestamp = datetime.now()
    
    session_ID = random_number
    numbers = 122
    serial = "12asa121a2"
    date = (timestamp.strftime("%Y-%m-%d"))
    session_start_time = (timestamp.strftime("%Y-%m-%d"))
    session_end_time = (timestamp.strftime("%Y-%m-%d"))
    session_status = 1
    temp_highest_level = 45
    temp_lowest_level = 36
    humidity_highest_level = 22
    humidity_lowest_level = 20
    try:
        session_data_object = session_data.objects.create(
            session_ID = random_number,
            numbers = 122,
            serial = "12asa121a2",
            date = (timestamp.strftime("%Y-%m-%d")),
            session_start_time = (timestamp.strftime("%Y-%m-%d")),
            session_end_time = (timestamp.strftime("%Y-%m-%d")),
            session_status = 1,
            temp_highest_level = 45,
            temp_lowest_level = 36,
            humidity_highest_level = 22,
            humidity_lowest_level = 20
        )

        session_data_object.save()
    except Exception as err:
        print(err)
    return render(request,"Dashboard.html")


def addGroups(request):
    pass

# login,  ajax for continuous data of micro cont* 
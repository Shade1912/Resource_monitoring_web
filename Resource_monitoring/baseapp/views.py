from collections import UserString
from datetime import datetime, time
from plistlib import UID
import random
from django.shortcuts import render, redirect
from baseapp.models import group_privileges
from baseapp.models import session_data
from django.db.models import Q

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

# Model Structure

# Device Model
# Device UID
# device id
# channel/probe 1
# channel/probe 2
# channel/probe 3
# channel/probe 4
# channel/probe 5
# channel/probe 6
# channel/probe 7
# channel/probe 8
# Device Location

# all Function structuresv

def checkPrivilege(GroupName, FunctionName):
    try:
        Access_Permission = group_privileges.objects.get(Q())
        return Access_Permission
    except Exception as err:
        print(err)

# def addLog(User, Log):
#     Add Log and User to table with time

# def addGroup(GroupName, Array containing all privilege values in order):
#     Add entry containing GroupName and Array

# def deleteGroup(GroupName):
#     Delete entry with GroupName

# def addUser(UserName,Password,GroupName):
#     Add entry containing UserName, Password, GroupName

# def deleteUser(UserName):
#     delete entry with UserName

# def fetchSessions():
#     fetch all ongoing sessions

# def listUsers():
#     list all Users

# def listGroup():
#     list all Groups

# def addAlert():
#     Add alert

# def deleteAlert():
#     delete alert

# def fetchGodownInfo():
#     fetch godown info noted in the app









# login,  ajax for continuous data of micro cont* 
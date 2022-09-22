from collections import UserString
from datetime import datetime, time
from imaplib import Commands
from os import access
from plistlib import UID
import random
from re import template
from django.shortcuts import render, redirect
from Resource_monitoring.baseapp.models import probe
from baseapp.models import group_privileges,userlogs,deleteGroup, alerts
from baseapp.models import session_data
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# view - Home, Login, Logout, User Management, addSession, monitoring, alerts, reports, channel info,  

def check_access(token, func_name):
    pass

def home(request):
    pass

@login_required
def dashboard(request):
    # Sessionkey => (request.session._session_key)
    
    return render(request,"./Dashboard.html")

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

# all Function structures
                        # Function use case
                        # checkPrivilege("Admin","print_report")
                        # addLog(request.user,"Test")
def checkPrivilege(GroupName, FunctionName):
    try:
        Access_Permission = group_privileges.objects.values_list(FunctionName).get(Q(group_name = GroupName))
        return Access_Permission[0]
    except Exception as err:
        print(err)
        return 0

def addLog(user, user_log):
    # Add Log and User to table with time
    try:
        user_log_query = userlogs.objects.create(
            username = user,
            logs = user_log
        )
        user_log_query.save()
        return 1
    except Exception as err:
        print(err)
        return 0

# def addGroup(GroupName, Array containing all privilege values in order):
#     Add entry containing GroupName and Array
# input-> addGroup(user,{print_view:1,addUser:0......})
# ouput-> if stored in db return 1 else print error and return 0 (refer userLog and checkPrivileges function)

userAccess = {
    "print_report" : 0,
    "view_time_table" : 0,
    "view_channel_info" : 0, 
    "create_user" : 0, 
    "delete_user" : 0, 
    "create_grp" : 0, 
    "delete_grp" : 0, 
    "grp_list" : 0, 
    "add_session" : 0, 
    "delete_session" : 0
}

def addGroup(groupName, userAccess):
    try:
        create_group_query = group_privileges.objects.create(
                group_name = groupName,
                print_report = userAccess.print_report,
                view_time_table = userAccess.view_time_table,
                view_channel_info = userAccess.view_channel_info,
                create_user = userAccess.create_user,
                delete_user = userAccess.delete_user,
                create_grp = userAccess.create_grp,
                delete_grp = userAccess.delete_grp,
                grp_list = userAccess.grp_list,
                add_session = userAccess.add_session,
                delete_session = userAccess.delete_session
        )
        create_group_query.save()
        return 1
    except Exception as err:
        print(err)
        return 0
    

# def deleteGroup(GroupName):
#     Delete entry with GroupName
# input->deleteGroup('user')
# ouput-> if deleted in db return 1 else print error and return 0 (refer userLog and checkPrivileges function)
def deleteGroup(groupName):
    try:
        group_privileges.objects.filter(group_name = groupName).delete()
        return 1
    except Exception as err:
        print(err)
        return 0

# def addUser(UserName,Password,GroupName):
#     Add entry containing UserName, Password, GroupName
# input-> addUser(Vat,123,User) -> AuthUser table and user_extra_details table must be used
# ouput-> if stored in db return 1 else print error and return 0 (refer userLog and checkPrivileges function)
def createUser(user_name,Password,group_Name):
    try:
        add_user_query = User.objects.create(
            userName = user_name,
            password = Password,
            groupName = group_Name
        )
        add_user_query.save()
    except Exception as err:
        print(err)
        return 0


# def deleteUser(UserName):
#     delete entry with UserName
# input-> deleteUser(vat)-> delete the entire row containing username as vat
# o/p-> try=> ret 1; except => print err and ret 0
def removeUser(user_name):
    try:
        User.objects.filter(userName = user_name).delete()
        return 1
    except Exception as err:
        print(err)
        return 0

# def fetchSessions():
#     fetch all ongoing sessions
# input fetchSession()=> it will get data of session
# o/p-> try=> ret session; except => print err and ret 0
def fetchSessions(request):
    try:
        sessionData = session_data.objects.all()
        return render(request,"showSession.html",{'Session Data':sessionData})
    except Exception as err:
        print(err)
        return 0

# def listUsers():
#     list all Users
# o/p-> try=> ret list; except => print err and ret 0
def listUsers(request):
    try:
        listUsers = User.objects.all()
        return render(request,"showUser.html",{'User Data':listUsers})
    except Exception as err:
        print(err)
        return 0

# def listGroup():
#     list all Groups
# o/p-> try=> ret list; except => print err and ret 0
def listGroup(request):
    try:
        groupData = group_privileges.objects.all()
        return render(request,"showGroup.html",{'Group Data':groupData})
    except Exception as err:
        print(err)
        return 0

# def addAlert():
#     Add alert
# o/p-> try=> ret 1; except => print err and ret 0
def addAlert(session_Id, Temperature, Humidity, temperature_In_Range, humidity_In_Range):
    try:
        add_alert_query = alerts.objects.create(
            session_id = session_Id,
            temperature = Temperature,
            humidity = Humidity,
            temperature_in_range = temperature_In_Range,
            humidity_in_range = humidity_In_Range
        )
        add_alert_query.save()
        return 1
    except Exception as err:
        print(err)
        return 0

# def deleteAlert():
#     delete alert
# o/p-> try=> ret 1; except => print err and ret 0
def removeAlert(sessionID):
    try:
        alerts.objects.filter(session_id = sessionID).delete()
        return 1
    except Exception as err:
        print(err)
        return 0


# def deleteSession():
#     delete session
# o/p-> try=> ret 1; except => print err and ret 0
def removeSession(sessionID):
    try:
        session_data.objects.filter(session_ID = sessionID).delete()
        return 1
    except Exception as err:
        print(err)
        return 0


# def fetchLogs():
#     fetch godown info noted in the app
# o/p-> try=> ret logs; except => print err and ret 0

#------------------------------------ new-structures ------------------------------------#

# def syncData():
#     Run all sync Commands

# def syncUserLogs():
#     sync user log table

# def syncDrugTemplate():
#     sync drug template table

# def syncProbe():
#     sync probe table

# def syncDevice():
#     sync device table

# def syncSessionData():
#     sync session data table



# login,  ajax for continuous data of micro cont* 
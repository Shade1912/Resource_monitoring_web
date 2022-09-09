from collections import UserString
from datetime import datetime, time
from os import access
from plistlib import UID
import random
from django.shortcuts import render, redirect
from baseapp.models import group_privileges,userlogs
from baseapp.models import session_data
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

# all Function structuresv
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
    

# def deleteGroup(GroupName):
#     Delete entry with GroupName
# input->deleteGroup('user')
# ouput-> if deleted in db return 1 else print error and return 0 (refer userLog and checkPrivileges function)

# def addUser(UserName,Password,GroupName):
#     Add entry containing UserName, Password, GroupName
# input-> addUser(Vat,123,User) -> AuthUser table and user_extra_details table must be used
# ouput-> if stored in db return 1 else print error and return 0 (refer userLog and checkPrivileges function)

# def deleteUser(UserName):
#     delete entry with UserName
# input-> deleteUser(vat)-> delete the entire row containing username as vat
# o/p-> try=> ret 1; except => print err and ret 0

# def fetchSessions():
#     fetch all ongoing sessions
# input fetchSession()=> it will get data of session
# o/p-> try=> ret session; except => print err and ret 0


# def listUsers():
#     list all Users
# o/p-> try=> ret list; except => print err and ret 0

# def listGroup():
#     list all Groups
# o/p-> try=> ret list; except => print err and ret 0

# def addAlert():
#     Add alert
# o/p-> try=> ret 1; except => print err and ret 0

# def deleteAlert():
#     delete alert
# o/p-> try=> ret 1; except => print err and ret 0


# def deleteSession():
#     delete session
# o/p-> try=> ret 1; except => print err and ret 0


# def fetchLogs():
#     fetch godown info noted in the app
# o/p-> try=> ret logs; except => print err and ret 0









# login,  ajax for continuous data of micro cont* 
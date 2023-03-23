from datetime import datetime, time
from imaplib import Commands
import random
from django.shortcuts import render, redirect
from baseapp.models import probe
from baseapp.models import group_privileges,userlogs, alerts,session_data, user_extra_details
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import sys
import glob
import serial
import threading
import time


def serialPort():
    ser = serial.Serial(
    port='COM2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=10)

    print("connected to: " + ser.portstr)
    return ser


def readData():
    ser = serialPort()
    data = ser.readline(50)
    print("initial data:",data)
    return data

def read_data_from_port():
    t = threading.Thread(target=readData)
    t.start()

read_data_from_port()
# from background_task import background


def check_access(token, func_name):
    pass

def home(request):
    pass

def addreses(request):
    return render(request,"./addresess.html")

def alert(request):
    alerts_query = alerts.objects.all()
    context = {
        "alerts":alerts_query
    }
    return render(request,"./alerts.html",context)

def monitoring(request):
    return render(request,"./Monitoring.html")

def reports(request):
    return render(request,"./Reports.html")
    
def timetable(request):
    return render(request, "./Timetable.html")

def channelinfo(request):
    prodeData = probe.objects.all()
    context = {
        "probeData":prodeData
    }
    return render(request, "./Channelinfo.html",context)

def uac(request):
    return render(request, "./UserAccessControl.html")

def addUser(request):
    groups_priv = group_privileges.objects.all()
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        group_priv_id = request.POST["group_priv_id"]
        createUser(firstname,lastname,email,username,password,group_priv_id)
    context = {
        "group_priv": groups_priv
    }
    return render(request, "./addUser.html",context)

def createUser(firstname,lastname,email,user_name,Password,group_Name):
    try:
        add_user_query = User.objects.create(
            username = user_name,
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = Password,
        )
        add_user_query.save()
        user_id = add_user_query.pk
        addUserExtraDetails(user_id, group_Name)
        return "Creating User..."
    except Exception as err:
        print(err)
        return "Error creating user"

def addUserExtraDetails(userId , groupName):
    try:
        print("Extra details of user")
        user_extra_details_query = user_extra_details.objects.create(
            user_id = User.objects.get(pk=userId),
            group_name = group_privileges.objects.get(pk = groupName),
            is_deleted = 0,
            session_tokens = "",
        )
        user_extra_details_query.save()
        return "User created"
    except Exception as err:
        print("Error:", err)
        return "Error creating user, try again later"



def manageUser(request):
    return render(request, "./Manageusers.html")
    
def delUser(request):
    all_user = user_extra_details.objects.filter(is_deleted=0)
    context = {
        "all_users": all_user
    }
    return render(request, "./delUser.html",context)

def deleteUserLink(request,userId):
    user = user_extra_details.objects.get(pk = userId)
    user.is_deleted = 1
    user.save()
    return redirect(delUser)

def viewUser(request,userId):
    user_details = user_extra_details.objects.get(pk = userId)
    groups = group_privileges.objects.all()
    user_main_details = User.objects.get(pk = user_details.user_id.pk)
    context = {
        "user_details": user_details,
        "groups": groups
    }
    if request.method == "POST":
        print(request.POST['group'])
        user_main_details.username = request.POST['username']
        user_main_details.first_name = request.POST['firstname']
        user_main_details.last_name = request.POST['lastname']
        user_details.is_deleted = request.POST['deleteUser']
        user_details.group_name = group_privileges.objects.get(pk = request.POST['group'])
        user_details.save()
        user_main_details.save()
        return redirect("/editUser")

    return render(request, "./view_user.html",context)

def editUser(request):
    all_user = user_extra_details.objects.filter(is_deleted = 0)
    context = {
        "all_users": all_user
    }
    return render(request, "./editUser.html",context)


def manageGroup(request):

    return render(request, "./Managegroups.html")
   
def addGroupPage(request):
    if request.method == "POST":
        permArray = list(request.POST["permArray"])
        group_name = request.POST['groupName']
        add_group = group_privileges.objects.create(
            group_name = group_name,
            print_report = permArray[0],
            view_time_table = permArray[1],
            view_channel_info = permArray[2],
            create_user = permArray[3],
            delete_user = permArray[4],
            create_grp = permArray[5],
            delete_grp = permArray[6],
            grp_list = permArray[7],
            add_session = permArray[8],
            delete_session = permArray[9],
        )
        add_group.save()
        # print(permArray)
    return render(request, "./addGroup.html")


def editGroup(request):
    pass

def viewGroup(request):
    pass


@login_required
def dashboard(request):
    # Sessionkey => (request.session._session_key)
    return render(request,"./Dashboard.html")

def monitor(request):
    return render(request,"./Monitoring.html")    

def addSession(request):
    random_number = random.randint(0,500)
    timestamp = datetime.now()  
    print("adding session") 
    try:
        if request.method == "POST": 
            print("creating session")
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
            print("session created")
            session_data_object.save()
            print("session added")
    except Exception as err:
        print(err)
    return redirect(monitoring)

def addsess(request):
    return render(request,"./addsess.html")

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

# def Page(GroupName, Array containing all privilege values in order):
#     Add entry containing GroupName and Array
# input-> Page(user,{print_view:1,addUser:0......})
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

def Page(groupName, userAccess):
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
        print(sessionData)
        return render(request,"./showSession.html",{'SessionData':sessionData})
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
def removeSession(request,sessionID):
    try:
        if request.method == "POST":
            print("sessionn data deleting")
            remove_session_query = session_data.objects.filter(session_ID = sessionID).delete()
            print(remove_session_query)
            # remove_session_query.save()
            return redirect(monitoring)
    except Exception as err:
        print(err)
        return redirect(monitoring)
    


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


def testPage(request):
    return render(request,"./test.html")
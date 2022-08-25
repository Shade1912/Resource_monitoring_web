from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    pass

def dashboard(request):
    return render(request,"Dashboard.html")

def addSession(request):
    
    pass

#  session_ID = models.CharField(max_length=10,primary_key=True)
#     numbers = models.IntegerField()
#     serial = models.CharField(max_length=20)
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     session_start_time = models.CharField(max_length= 15)
#     session_end_time = models.CharField(max_length=15)
#     session_status = models.BooleanField()
#     temp_highest_level = models.FloatField()
#     temp_lowest_level = models.FloatField()
#     humidity_highest_level = models.FloatField()
#     humidity_lowest_level = models.FloatField()
#     time_interval = models.TimeField(default= "00:00:00")

def addGroups(request):
    pass

# login, 
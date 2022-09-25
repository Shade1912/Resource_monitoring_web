from django.urls import path
from baseapp import views

urlpatterns = [
    # path('/', views.home, name="home"),
    path('', views.dashboard, name="dashboard"),
    path('addreses', views.addreses, name="addreses"), 
    path('alert', views.alert, name="alert"), 
    path('monitoring', views.monitoring, name="monitoring"), 
    path('reports', views.reports, name="reports"), 
    path('timetable', views.timetable, name="timetable"), 
    path('channelinfo', views.channelinfo, name="channelinfo"), 
    path('addSession', views.addSession, name="addSession"), 
    path('uac', views.uac, name="uac"), 
    path('addUser/<str:name>/<str:email>/<str:password>/<str:grp_name>', views.addUser, name="addUser"), 
    path('removeSession/<slug:sessionID>', views.removeSession, name="removeSession"), 

]
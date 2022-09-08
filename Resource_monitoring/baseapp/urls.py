from django.urls import path
from ..baseapp import views

urlpatterns = [
    # path('/', views.home, name="home"),
    path('', views.dashboard, name="dashboard"),
]
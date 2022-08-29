from django.urls import path
from ..baseappp import views

urlpatterns = [
    # path('/', views.home, name="home"),
    path('', views.dashboard, name="dashboard"),
]
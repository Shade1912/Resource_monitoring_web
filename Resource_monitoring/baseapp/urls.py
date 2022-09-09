from django.urls import path
<<<<<<< Updated upstream
from ..baseapp import views
=======
from baseapp import views
>>>>>>> Stashed changes

urlpatterns = [
    # path('/', views.home, name="home"),
    path('', views.dashboard, name="dashboard"),
]
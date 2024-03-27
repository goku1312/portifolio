
from django.urls import path
from app import views


urlpatterns = [

    path("",views.home),
    path("home",views.home),
    path("homemail",views.homemail),
]
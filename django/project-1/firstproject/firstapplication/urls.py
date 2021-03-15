from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello, name="hello"),
    path('bye/',views.bye, name="bye"),
    path('welcome/',views.welcome, name="welcome"),
    path('login/',views.login, name="login"),
    path('login/welcome/',views.welcome, name="welcome"),
    path('welcome-info/', views.info, name="info")
]

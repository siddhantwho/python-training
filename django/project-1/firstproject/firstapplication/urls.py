from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello, name="hello"),
    path('bye/',views.bye, name="bye")
]

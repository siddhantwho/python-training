from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.blog_list, name='blog_list')
]

from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view/<int:pk>', views.blog_view, name='blog_post'),
    path('create', views.blog_create, name='blog_create'),
    path('edit/<int:pk>', views.blog_update, name='blog_edit'),
    path('delete/<int:pk>', views.blog_delete, name='blog_delete')
]

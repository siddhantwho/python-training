from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Blog

# Create your views here.

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','author','time','post']

def blog_list(request, template_name='list.html'):
    blog = Blog.objects.all()
    data = {}
    data['object_list'] = blog
    
    return render(request, template_name, data)



 
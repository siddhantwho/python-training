from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Blog
from django import forms

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

def blog_view(request, pk, template_name='blogpost.html'):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, template_name, {'object': blog})

def blog_create(request, template_name='blogform.html'):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form': form})

def blog_update(request, pk, template_name='blogform.html'):
    blog= get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_delete(request, pk, template_name='blogdelete.html'):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name, {'object':blog})
 
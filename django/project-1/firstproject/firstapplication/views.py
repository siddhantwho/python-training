from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, Person_Form

# Create your views here.
def hello(request):
    return HttpResponse("Hello world!")

def bye(request):
    return HttpResponse("Bye world!")

def welcome(request):
    return render(request, "page1.html")

def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, "page2.html", context)

def info(request):
    form = Person_Form(request.POST, use_required_attribute=False)
    if form.is_valid():
        form.save()
        form = Person_Form()
    context = {'form': form}
    return render(request, "page1.html", context)
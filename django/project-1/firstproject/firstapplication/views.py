from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello world!")

def bye(request):
    return HttpResponse("Bye world!")

def view1(request):
    return render(request,"page1.html")
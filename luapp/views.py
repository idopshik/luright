from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'luapp/about.html')
    #  return HttpResponse('<h1> Hello django </h1>')

def home(request):
    return render(request, 'luapp/home.html')

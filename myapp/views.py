import re
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def getdata(request):
    return HttpResponse("Get Data")
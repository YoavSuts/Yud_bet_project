from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    #C:\Cyber_Stock_project\Bot_code\mysite\mysite\templates
    abs_path = os.path.dirname(__file__)
    rpath = "mysite/mysite/templates/mysite/home.html"
    full_path = os.path.join(abs_path, rpath)
    return render(request,  r"mysite/home.html")
    #return HttpResponse("yahli")
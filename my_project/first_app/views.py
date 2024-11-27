from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return HttpResponse("this is demo app")
def about(request):
    return HttpResponse("this is about section")
def home(request):
    return HttpResponse("this is home section")


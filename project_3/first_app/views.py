from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {
        "author": "Arnob",
        "age": 20,
        'birthday' : datetime.datetime.now(),
        'lst' : ['python', 'is', 'fun'],
        'val' : " ",
        "courses": [
            {
                "id": 1,
                "name": "OOP",
                "fees": 1000,
            },
            {
                "id": 2,
                "name": "PPS",
                "fees": 1500,
            },
            {
                "id": 3,
                "name": "EEE",
                "fees": 2000,
            },
        ],
    }
    return render(request, "home.html", d)

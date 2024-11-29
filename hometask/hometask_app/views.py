from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    d = {
        "author": "Arnob",
        "age": 20,
        "lst": ["CODING", "IS", "LOVE"],
        "birthday": datetime.datetime.now(),
        "page": "myFIRSTpost",
        "val": "",
        "courses": [
            {"id": 1, "name": "DSA", "fee": 5500},
            {"id": 2, "name": "MySQL", "fee": 500},
            {"id": 3, "name": "Django", "fee": 3000},
        ],
        "diff": [
            {"name": "Josh", "age": 42},
            {"name": "Dave", "age": 22},
            {"name": "Joe", "age": 31},
        ],
    }
    return render(request, "home.html", d)

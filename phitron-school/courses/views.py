from django.shortcuts import render

# Create your views here.
def get_course(request):
    return render(request, 'base.html') 

def profile(request):
    return render(request, "profile.html")

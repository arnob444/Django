from django.shortcuts import render,redirect
from .forms import demoForm
from . import forms
from . import models

def home(request):
    demo = models.Mymodel.objects.all()
    return render(request, 'home.html', {'data' : demo})


def submit_form(request):
    if request.method == 'POST':
        form = forms.demoForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('homepage')
            print(form.cleaned_data)
    else:
        form = forms.demoForm()
    return render(request, 'form.html', {'form' : form})
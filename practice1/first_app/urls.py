from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path('form/', views.submit_form, name='submit_form')
]

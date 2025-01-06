from django import forms 
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class demoForm(forms.Form):
    name = forms.CharField(label= "Enter your name: ")
    email = forms.EmailField(label = "User Email")
    comment = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10, help_text="maximum length 10")
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today, label='Todays Date')
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    fav_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    fav_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    multi_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    password = forms.CharField(widget = forms.PasswordInput()) 

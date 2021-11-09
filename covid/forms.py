from django import forms
from django.contrib.auth.models import User
from .models import organization, department, recordss
from django.forms import ModelChoiceField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class DataForm(forms.Form):
    Sr_no = forms.IntegerField()
    name = forms.CharField(max_length=25)
    designation = forms.CharField(max_length=25, required=False)
    last_vaccine_date = forms.DateField(widget = forms.SelectDateWidget, required=False)
    no_of_vaccines_taken = forms.IntegerField(max_value=2, min_value=0)
    CHOICES = [('negative', 'negative'),
                ('positive', 'positive')]
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    covid_test_date = forms.DateField(widget = forms.SelectDateWidget, required=False)
    vaccine_certificate_beneficiary_id = forms.IntegerField(required=False)

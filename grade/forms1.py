from django import forms
from django.forms import fields

class ADD_form(forms.Form):
    a=forms.FileField()
from django import forms 

class Weatherform(forms.Form):
    city = forms.CharField(label="enter city name",max_length=30)
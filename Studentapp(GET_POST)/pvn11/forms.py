from django import forms
class StudentAppa(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    marks=forms.IntegerField()

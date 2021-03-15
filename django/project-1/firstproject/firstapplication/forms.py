from django import forms
from .models import Person

class LoginForm(forms.Form):

    name = forms.CharField(label="Name: ", max_length=20)
    email = forms.EmailField(label="Email: ", max_length=20)

class Person_Form(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
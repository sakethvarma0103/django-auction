from django import forms
from .models import Login,Signup

class LoginForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ['user_name', 'password']
        labels = {
            "user_name": "Your Name",
            "password": "Password",
        }

class SignForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "password": "Password",
        }
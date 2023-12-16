from django.shortcuts import render,redirect
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_page(request):
    if request.method=="POST":
        username=request.POST["user_name"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('auction')
        else:
            return HttpResponseRedirect('login')
    else:
        form=LoginForm()
    return render(request,"login.html",{
        "form":form
    })

def sign(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('auction')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{
        "form":form
    })

def logout_user(request):
    logout(request)
    return redirect("login_page")
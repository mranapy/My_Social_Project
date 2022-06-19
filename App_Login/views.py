from django.shortcuts import render
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

# Create your views here.

def signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            pass
    return render(request, 'App_login/signup.html',context={'title':'Sign Up Instragram','form':form})

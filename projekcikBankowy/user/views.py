from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from .forms import RegisterForm
from .models import Client
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.http import HttpResponseRedirect

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            id = form.cleaned_data['id']
            password = form.cleaned_data['password1']
            try:
                User.objects.get(username=email)
            except User.DoesNotExist:
                c = Client(first_name=first_name, last_name=last_name, id=id, email=email, password=password, balance=0.0, account_number="2598 0000 2030" + str(id))
                c.save()
                user = User.objects.create_user(email,email=email,password=password)
                user.save()
                return render(request, "user/register_complete.html")
            messages.error(request, "Email is already in use. Please use another Email\n")
            return render(request, "user/register.html", {'form': form})
    else:
        form = RegisterForm()

    return render(request, "user/register.html", {'form': form})

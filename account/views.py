from django.shortcuts import render, redirect
from django.contrib.auth import login as log, authenticate 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from lecturer.models import Secret

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                log(request, user)
            if'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/accounts/go/')
        else:
            messages.error(request, 'Username or Password Mismatch!')
            return render(request, 'account/login.html', 
            {'username': request.POST['username'], 'password': request.POST['password']})
    else:
        return render(request, "account/login.html")


def secret_code(request, *args):
    if request.method == 'POST':
        try:
            secret = Secret.objects.get(secret=request.POST['secret'])
            if'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/')
        except:
            return redirect('/home/')
    else:
        return render(request, "account/secret.html")
        

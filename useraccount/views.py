from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.shortcuts import redirect, render
from .forms import LoginForm
from premium.models import Premium

# *** remove once implemented logout view ***
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Create a new Premium object upon registering
            username = form.cleaned_data['username']
            new_user = User.objects.get(username=username)
            users_premium = Premium(user_id=new_user.id)
            users_premium.save()
            return redirect('recipe:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'useraccount/register.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                user_login(request, user)
                return redirect('recipe:index')
            else:
                return redirect('useraccount:login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'useraccount/login.html', context)

def logout(request):
    user_logout(request)
    return redirect('recipe:index')

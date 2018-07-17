from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# *** remove once implemented logout view ***
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'from': form}
    return render(request, 'useraccount/register.html', context)

def login(request):
    return render(request, 'useraccount/login.html')

def logout(request):
    logout(request)
    return redirect('index')

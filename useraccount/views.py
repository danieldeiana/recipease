from django.shortcuts import render

from django.http import HttpResponse

def register(request):
    return render(request, 'useraccount/register.html')

def login(request):
    return render(request, 'useraccount/login.html')

def logout(request):
    return HttpResponse('this is where to logout')
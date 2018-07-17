from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index view")

def detail(request, meal_id):
    return HttpResponse("This is the detail view with meal id: {}".format(meal_id))
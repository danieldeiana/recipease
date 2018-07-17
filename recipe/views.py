from django.shortcuts import render
from .models import Meal

from django.http import HttpResponse

def index(request):
    meals = Meal.objects.all()
    context = {'meals': meals,}
    return render(request, 'recipe/index.html', context)

def detail(request, meal_id):
    return HttpResponse("This is the detail view with meal id: {}".format(meal_id))
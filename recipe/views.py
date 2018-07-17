from django.shortcuts import get_object_or_404, render
from .models import Meal

def index(request):
    meals = Meal.objects.all()
    context = {'meals': meals,}
    return render(request, 'recipe/index.html', context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, 'recipe/detail.html', {'meal': meal})

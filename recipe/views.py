from django.shortcuts import get_object_or_404, render
from .filters import MealFilter
from .models import Meal

def index(request):
    meal_list = Meal.objects.all()
    meal_filter = MealFilter(request.GET, queryset=meal_list)
    context = {'filter': meal_filter}
    return render(request, 'recipe/index.html', context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, 'recipe/detail.html', {'meal': meal})

from django.shortcuts import get_object_or_404, render
from .filters import MealFilter
from .models import Meal
from premium.models import Premium

def index(request):
    meal_list = Meal.objects.all()
    meal_filter = MealFilter(request.GET, queryset=meal_list)
    current_user = request.user
    premium = {}
    if current_user.username:
        premium = Premium.objects.get(user_id=current_user.id)
    context = {
        'filter': meal_filter,
        'premium': premium,
        }

    return render(request, 'recipe/index.html', context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    current_user = request.user
    premium = {}
    if current_user.username:
        premium = Premium.objects.get(user_id=current_user.id)
    context = {
        'meal': meal,
        'premium': premium}
    return render(request, 'recipe/detail.html', context)

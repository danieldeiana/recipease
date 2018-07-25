from django.shortcuts import get_object_or_404, render
from .filters import MealFilter
from .models import Meal
from premium.forms import CommentForm
from premium.models import Premium

def index(request, favourites=None):
    if favourites:
        premium_user = Premium.objects.get(user_id=request.user.id)
        favourite_id_list = premium_user.favourite_id_list
        meal_list = Meal.objects.filter(id__in=favourite_id_list)
    else:    
        meal_list = Meal.objects.all()


    meal_filter = MealFilter(request.GET, queryset=meal_list)
    current_user = request.user
    premium = {}
    if current_user.username:
        try:
            premium = Premium.objects.get(user_id=current_user.id)
        except:
            new_premium = Premium(user_id=current_user.id)
            new_premium.save()
            premium = new_premium
    context = {
        'filter': meal_filter,
        'premium': premium,
        }

    return render(request, 'recipe/index.html', context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    current_user = request.user
    premium = {}
    comment_form = CommentForm()
    if current_user.username:
        premium = Premium.objects.get(user_id=current_user.id)
    context = {
        'meal': meal,
        'premium': premium,
        'comment_form': comment_form,
        }
    return render(request, 'recipe/detail.html', context)

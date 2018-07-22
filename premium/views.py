from decouple import config
from django.shortcuts import  redirect, render
import stripe
from premium.models import Premium
from recipe.models import Meal

stripe.api_key = config('STRIPE_APIKEY')

def payment(request):
    # If user authenticated, render stripe form and return auth' token
    if not request.user.is_authenticated:
        return redirect('recipe:index')
    return render(request, 'premium/payment.html')

def process(request):
    # Process payment with stripe auth' token
    token = request.POST['stripeToken']
    stripe.Charge.create(
        amount=99,
        currency="gbp",
        description="premium content, Recipease",
        source=token,
    )
    current_user = request.user
    users_premium = Premium.objects.get(user_id=current_user.id)
    users_premium.activated = True
    users_premium.save()
    return redirect('recipe:index')

def add_favourite(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    current_user = request.user
    users_premium = Premium.objects.get(user_id=current_user.id)
    users_premium.favourites.add(meal)
    return redirect('recipe:detail', meal_id)

def remove_favourite(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    current_user = request.user
    users_premium = Premium.objects.get(user_id=current_user.id)
    users_premium.favourites.remove(meal)
    return redirect('recipe:detail', meal_id)
from decouple import config
from django.contrib.auth.models import User
from django.shortcuts import  redirect, render
import stripe
from premium.models import Premium
from premium.forms import CommentForm
from recipe.models import Comment, Meal

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

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_id = form.cleaned_data['user_id']
            meal_id = form.cleaned_data['meal_id']

            meal = Meal.objects.get(id=meal_id)
            user = User.objects.get(id=user_id)

            new_comment = Comment(user=user, text=text)
            new_comment.save()
            meal.comment.add(new_comment)
            meal.save()

            return redirect('recipe:detail', meal_id)
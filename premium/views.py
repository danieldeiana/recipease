from django.shortcuts import  redirect, render
from decouple import config
import stripe

stripe.api_key = config('STRIPE_APIKEY')

# !!! delete once views are fully implemented with render !!!
from django.http import HttpResponse

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
    return HttpResponse('Thanks, your payment was successfull')
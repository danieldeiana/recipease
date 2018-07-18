from django.urls import path

from . import views

app_name = 'premium'
urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('process/', views.process, name='process')
    ]

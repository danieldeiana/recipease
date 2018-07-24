from django.urls import path

from . import views

app_name = 'premium'
urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('process/', views.process, name='process'),
    path('addfavourite/<int:meal_id>', views.add_favourite, name='add_favourite'),
    path('removefavourite/<int:meal_id>', views.remove_favourite, name='remove_favourite'),
    path('comment/', views.comment, name='comment'),
    ]

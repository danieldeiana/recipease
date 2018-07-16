from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=60)
    intro = models.CharField(max_length=180)
    image = models.ImageField(upload_to = 'meal_images/')
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    user_rating = models.IntegerField()

    def __str__(self):
        return self.name
    
    def total_time(self):
        return self.cooking_time + self.preparation_time

class Category(models.Model):
    name = models.CharField(max_length=30)
    meal = models.ManyToManyField(Meal)

class Ingredient(models.Model):
    MEASUREMENT_CHOICES = (
        ('tsp', 'teaspoon'),
        ('tbsp', 'tablespoon'),
        ('oz', 'fluid ounce'),
        ('ml', 'millilitre'),
        ('l', 'litre'),
        ('ib', 'pound'),
        ('oz', 'ounce'),
        ('mg', 'milligram'),
        ('g', 'gram'),
        ('kg', 'kilogram'),
        ('cm', 'centimeter'),
        ('sml', 'small'),
        ('med', 'medium'),
        ('lrg', 'large'),
    )
    name = models.CharField(max_length=30)
    measurement = models.CharField(choices=MEASUREMENT_CHOICES, max_length=30)
    quantity = models.IntegerField()
    meal = models.ManyToManyField(Meal)

class Step(models.Model):
    text = models.TextField(max_length=120)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

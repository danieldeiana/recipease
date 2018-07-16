from django.contrib import admin

from .models import Category, Comment, Ingredient, Meal, Step

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(Step)

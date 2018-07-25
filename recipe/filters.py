from .models import Meal
import django_filters

class MealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='contains',
        label='Search Recipes',
        )
    class Meta:
        model = Meal
        fields = [
            'name',
            'category',
            'ingredient',
        ]

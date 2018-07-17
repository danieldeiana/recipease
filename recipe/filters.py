from .models import Meal
import django_filters

class MealFilter(django_filters.FilterSet):
    USER_RATING_CHOICES = (
        [(x+1, x+1) for x in range(5)]
    )
    name = django_filters.CharFilter(
        lookup_expr='contains',
        label='Search Recipes',
        )
    user_rating = django_filters.ChoiceFilter(
        choices=USER_RATING_CHOICES,
        )
    class Meta:
        model = Meal
        fields = [
            'name',
            'user_rating',
            'category',
            'ingredient',
        ]

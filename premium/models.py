from django.db import models
from recipe.models import Meal

class Premium(models.Model):
    user_id = models.IntegerField(unique=True)
    activated = models.BooleanField(default=False)
    favourites = models.ManyToManyField(Meal)

    @property
    def favourite_id_list(self):
        ids = []
        for meal in self.favourites.all():
            ids.append(meal.id)
        return ids
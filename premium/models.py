from django.db import models

class Premium(models.Model):
    user_id = models.IntegerField(unique=True)
    activated = models.BooleanField(default=False)
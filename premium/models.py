"""
Had a very hard time trying to setup a OneToOne field related to the User model
Followed Vitor's example but it did'nt want to work..
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone (option two)

After a couple of day's of pain, instead of wasting more time I've decided to link the models using user.id
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone (option one)
"""

from django.contrib.auth.models import User
from django.db import models

class Premium(models.Model):
    user_id = models.IntegerField(unique=True)
    activated = models.BooleanField(default=False)

class PremiumUser(User):
    """
    Get an instance of a premium user. It's from the same database as the inherited User model
    as this is a proxy model of User:
        $ bob = PremiumUser.objects.get(username='bob')
    
    See is he's activated for premium:
        $ bob.activated
            false
        
    Deactivate and activate with these methods:
        $ bob.activate()
        $ bob.deactivate()
    """
    class Meta:
        proxy = True

    def get_or_create_premium_object(self):
        """
        Get the Premium model object where Premium.user_id == User(self).id
        If it doesn't exist, create and save a new Premium object for the current user
        Return the Premium object in both instances
        """
        try:
            p = Premium.objects.get(user_id=self.id)
            return p
        except models.ObjectDoesNotExist:
            p = Premium(user_id=self.id)
            p.save()
            return p

    @property
    def is_member(self):
        """
        Retrieve the users(self) Premium object and return the activated attribute
        """
        p = self.get_or_create_premium_object()
        return p.activated

    def activate(self):
        """
        Retrieve the users(self) Premium object, set the activated attribute to True and save
        """
        p = self.get_or_create_premium_object()
        p.activated = True
        p.save()
    
    def deactivate(self):
        """
        Retrieve the users(self) Premium object, set the activated attribute to False and save
        """
        p = self.get_or_create_premium_object()
        p.activated = False
        p.save()
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Auction(models.Model):
       CATEGORIES = (
           ('LAP', 'Laptop'),
           ('CON', 'Console'),
           ('GAD', 'Gadget'),
           ('GAM', 'Game'),
           ('TEL', 'TV')
       )

       title = models.CharField(max_length=255)
       price = models.IntegerField()
       description = models.CharField(max_length = 500)
       quantity = models.IntegerField()
       category = models.CharField(
           max_length=22,
           choices=CATEGORIES
       )
       date_posted = models.DateTimeField(auto_now_add=True, blank=True)

       def __str__(self):
           return f"{self.id}: {self.title} {self.price} {self.quantity} {self.category}"

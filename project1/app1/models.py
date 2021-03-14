from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    name    = models.CharField(max_length=100)
    game    = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone   = models.BigIntegerField()
    time    = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User, on_delete=models.CASCADE) #create a one-to-many relationship beween user and associated posts.



# models.DateTimeField(
# auto_now=True             -> this will update the field with the current date-time every time an update is made to the field.
# or auto_now_add=True      -> this will only take the date-time the field value was first entered and never again, not even when the field is updated with a value. 
# or default=timezone.now   -> 
# )
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)  # Automatically set on creation
    is_active = models.BooleanField(default=True)  # For user’s active status

    def __str__(self):
        return self.username


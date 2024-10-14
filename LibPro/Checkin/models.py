from django.db import models
from django.conf import settings
from Book.models import Book  # Assuming you already have a Book model

class Checkin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} returned {self.book.title}'




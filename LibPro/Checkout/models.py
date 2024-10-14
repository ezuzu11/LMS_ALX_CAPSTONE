from django.db import models
from django.conf import settings
from Book.models import Book

# Create your models here.

class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'book', 'is_returned'] # Ensures one copy per user till returned

    def __str__(self):
        return f'{self.user.username} checked out {self.book.title}'  

from rest_framework import serializers
from .models import Book
#from .models import Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError("ISBN must be either 10 or 13 characters.")
        return value

      
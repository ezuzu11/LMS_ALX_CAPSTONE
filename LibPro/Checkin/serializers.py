from rest_framework import serializers
from .models import Checkin

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ['user', 'book', 'return_date', 'is_returned']

    def create(self, validated_data):
        book = validated_data['book']
        if validated_data['is_returned']:
            book.copies_available += 1  # Increment the available copies when the book is returned
            book.save()
        return super().create(validated_data)

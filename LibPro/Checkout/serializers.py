from rest_framework import serializers
from .models import Checkout
from django.utils import timezone
from rest_framework.decorators import action
from django.contrib.auth import get_user_model

User = get_user_model()

class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  

    class Meta:
        model = Checkout
        fields = ['user', 'book', 'return_date', 'is_returned']

    def validate(self, data):
        book = data['book']
        if book.copies_available <= 0:
            raise serializers.ValidationError("No copies of the book are available for checkout.")
        return data

    @action(detail=True, methods=['POST'])
    def create(self, validated_data):
        book = validated_data['book']
        is_returned = validated_data['is_returned']
        if not is_returned:
            book.copies_available -= 1  # Reduce the available copies

        book.save()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        book = instance.book
        is_returned = validated_data.get('is_returned', instance.is_returned)
        

        # If the book is being returned and wasn't returned before
        if is_returned and not instance.is_returned:
            book.copies_available += 1
            validated_data['return_date'] = timezone.now()
            return 'Book returned successfully!'

        book.save()
        return super().update(instance, validated_data)

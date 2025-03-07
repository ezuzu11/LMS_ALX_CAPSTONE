from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ['username', 'email', 'date_of_membership', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # this helps to not return the password
        }
    
    def create(self, validate_data):
        user = User.objects.creare_user(
            username = validate_data['username'],
            email = validate_data['email'],
            password = validate_data['password']
        )
        return user
        

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)  # Gets the old password and being checked after
        if password:
            instance.set_password(password)
        
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance
 
 
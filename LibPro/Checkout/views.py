from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Checkout
from .serializers import CheckoutSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the checkout
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Ensure the user is still associated correctly on update
        serializer.save(user=self.request.user)


# creating a view that lists the transactions for the currently logged-in user

class UserBorrowingHistoryView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated] # this ensures only authenticated users can access 

    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)
    
    

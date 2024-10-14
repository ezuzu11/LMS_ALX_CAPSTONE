from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AvailableBooksListView
from django.urls import path



router = DefaultRouter()
router.register(r'Book', BookViewSet)



urlpatterns = router.urls

urlpatterns = [
    path('available-books/', AvailableBooksListView.as_view(), name= 'available-books'),
   
]
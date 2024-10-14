from rest_framework.routers import DefaultRouter
from .views import CheckoutViewSet, UserBorrowingHistoryView
from django.urls import path, include

router = DefaultRouter()
router.register(r'checkout', CheckoutViewSet)

urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls)),
    path('borrowing-history/', UserBorrowingHistoryView.as_view(), name='borrowing-history'),
]

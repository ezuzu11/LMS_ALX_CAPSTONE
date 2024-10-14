from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include
from django.contrib.auth import views as auth_views
'''
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
'''

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


'''
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    '''
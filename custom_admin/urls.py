from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from custom_admin.views import LoginView,LogoutView,RegisterView,ProfileView,Getallusersview,GetallresellersView,ActivenowView
urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('users/',Getallusersview.as_view()),
    path('resellers/',GetallresellersView.as_view()),
    path('active',ActivenowView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

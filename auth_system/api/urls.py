from django.urls import path
from .views import ListUsers, RetrieveUser, RegisterUser, ConfirmPassword, GenerateOtp, WelcomeView
urlpatterns = [
    path('', WelcomeView.as_view(), name = 'users'),
    path('api/<int:pk>', RetrieveUser.as_view(), name = 'user'),
    path('api/otp/<int:phone>', GenerateOtp.as_view(), name = 'otp'),
    path('api/register', RegisterUser.as_view(), name = 'register'),
    path('api/users', ListUsers.as_view(), name = 'profile'),
    path('password_reset_confirm', ConfirmPassword.as_view(), name = 'password_reset_confirm'),
]
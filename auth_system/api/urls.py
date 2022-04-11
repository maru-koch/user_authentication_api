from django.urls import path
from .views import ListUsers, RetrieveUser
urlpatterns = [
    path('', ListUsers.as_view(), name = 'users'),
    path('api/<int:pk>', RetrieveUser.as_view(), name = 'user'),
    path('register', RegisterUser.as_view(), name = 'register'),
    path('otp', RetrieveUser.as_view(), name = 'otp'),
    path('verify_otp', RetrieveUser.as_view(), name = 'verify_otp'),
    path('forgot_password', RetrieveUser.as_view(), name = 'forgot_password'),
    path('reset_password', RetrieveUser.as_view(), name = 'reset_password')
]
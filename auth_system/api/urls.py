from django.urls import path
from .views import ListUsers, RetrieveUser
urlpatterns = [
    path('', ListUsers.as_view(), name = 'users'),
    path('api/<int:pk>', RetrieveUser.as_view(), name = '')
]
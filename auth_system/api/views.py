from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from .models import CustomUser
from django.contrib.auth import permissions
from .serializer import ApiSerializer

class ListUsers(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer


class RetrieveUser(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer
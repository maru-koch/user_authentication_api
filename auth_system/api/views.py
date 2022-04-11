from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import CustomUser
from .serializer import ApiSerializer

class ListUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer


class RetrieveUser(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer
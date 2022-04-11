from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ListUsers(ListAPIView):
    pass

class RetrieveUser(RetrieveAPIView):
    pass
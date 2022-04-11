
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from .models import CustomUser

from .serializer import ApiSerializer

class ListUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer

class RegisterUser(CreateAPIView):
    serializer_class = ApiSerializer
    def create(self, request, username, email, first_name, last_name):
        user = CustomUser.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user.save()

class RetrieveUser(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from .models import CustomUser
from .serializer import ApiSerializer


class ListUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer


class RegisterUser(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers = headers)
        

class RetrieveUser(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer
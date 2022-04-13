
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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
    permission_classes = (IsAuthenticated)


class ConfirmPassword(UpdateAPIView):
    model = CustomUser
    serializer_class = ApiSerializer
    permission_classes = (IsAuthenticated)

    def get_object(self, queryset = None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


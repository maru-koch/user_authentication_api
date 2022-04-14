
from math import perm
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
import pyotp
from .models import CustomUser
from .serializer import ApiSerializer, ListSerializer
import random

#OTP
from datetime import datetime
import base64

class ListUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListSerializer
    
class WelcomeView(APIView):
    def get_object(self, queryset = None):
        obj = self.request.user
        return Response(obj)

class RegisterUser(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApiSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            serializer.save
        return Response("saved successfully", headers = headers)
        

class RetrieveUser(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListSerializer


class ConfirmPassword(UpdateAPIView):
    model = CustomUser
    serializer_class = ApiSerializer

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

class generateKey:
    @staticmethod
    def returnValue(phone):
        random_number = ''.join([str(random.randint(1, 9)), str(random.randint(1, 9)), str(random.randint(1, 9))])
        return str(phone) + str(datetime.date(datetime.now())) + random_number
        

class GenerateOtp(APIView):

    @staticmethod
    def get(request, phone):
        try:
            user = CustomUser.objects.get(phone = phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            return Response(f"No user with the Phone number: {phone}", status=404)
        else:
            user = CustomUser.objects.get(pk = request.user.id)
            user.phone = phone 
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
            OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
            # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
            return Response({"OTP": OTP.at(user.phone)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            phone = CustomUser.objects.get(phone=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], phone):  # Verifying the OTP
            phone.isVerified = True
            phone.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)

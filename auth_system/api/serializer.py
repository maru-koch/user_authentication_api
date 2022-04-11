from rest_framework import serializers
from .models import CustomUser

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        models = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

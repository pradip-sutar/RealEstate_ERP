from rest_framework import serializers
from .models import *

class EmployeePersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Profile
        fields = '__all__'

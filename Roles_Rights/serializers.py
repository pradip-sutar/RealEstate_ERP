from rest_framework import serializers
from .models import *

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class RightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rights
        fields = '__all__'

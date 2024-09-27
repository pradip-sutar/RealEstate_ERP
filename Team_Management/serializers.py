# serializers.py

from rest_framework import serializers
from .models import Team_Management

class TeamManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Management
        fields = '__all__'

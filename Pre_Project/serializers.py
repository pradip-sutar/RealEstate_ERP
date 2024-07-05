from rest_framework import serializers
from .models import *


class PreProjectNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreProjectNew
        fields = '__all__'

    
class ConfirmProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirm_Project
        fields = '__all__'
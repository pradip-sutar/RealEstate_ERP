from rest_framework import serializers
from .models import *


class PreProjectNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreProjectNew
        fields = '__all__'
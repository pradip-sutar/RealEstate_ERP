from rest_framework import serializers
from .models import *

class CustomerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Form
        fields = '__all__'

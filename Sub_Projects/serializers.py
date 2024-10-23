from rest_framework import serializers
from .models import *
# 1. Product Details Serializer
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

# 2. Raise Cost Serializer
class RaiseCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaiseCost
        fields = '__all__'

# 3. Product Cost Serializer
class ProductCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCost
        fields = '__all__'

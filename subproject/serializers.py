from rest_framework import serializers
from .models import *

# Serializer for Product Detail
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

# Serializer for Raise Cost
class RaiseCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaiseCost
        fields = '__all__'

# Serializer for Product Cost
class ProductCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCost
        fields = '__all__'
from rest_framework import serializers
from .models import ProductCost, AmenityCost

# Serializer for Product Cost
class ProductCost_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCost_1
        fields = '__all__'

# Serializer for Amenity Cost
class AmenityCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityCost
        fields = '__all__'

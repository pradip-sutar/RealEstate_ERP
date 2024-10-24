from rest_framework import serializers
from .models import *
# 1. Product Details Serializer
class ProductDetailsSerializer(serializers.ModelSerializer):
    segment_name = serializers.CharField(source='segment.name', read_only=True)
    product_type_name = serializers.CharField(source='product_type.name', read_only=True)
    varient_name = serializers.CharField(source='variant.name', read_only=True)
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
    product_type_name = serializers.CharField(source='product_type.name', read_only=True)
    varient_name = serializers.CharField(source='variant.name', read_only=True)
    class Meta:
        model = ProductCost
        fields = '__all__'

class ProductInventoriesSerializer(serializers.ModelSerializer):
    product_type_name = serializers.CharField(source='product_type.name', read_only=True)
    varient_name = serializers.CharField(source='variant.name', read_only=True)
    class Meta:
        model = ProductInventories
        fields = '__all__'

class SubProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProductImages
        fields = '__all__'

class PaymentSlabSerializer(serializers.ModelSerializer):
    segment_name = serializers.CharField(source='segment.name', read_only=True)
    class Meta:
        model = PaymentSlab
        fields = '__all__'
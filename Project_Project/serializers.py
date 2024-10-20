from rest_framework import serializers
from .models import *

class ProjectSubprojectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_subproject_details
        fields = '__all__'

# Commission Serializer
class ProjectCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Commission
        fields = '__all__'

# PaymentSlab Serializer
class ProjectPaymentSlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_PaymentSlab
        fields = '__all__'

# Tax Serializer
class ProjectTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Tax
        fields = '__all__'

# Amenity Serializer
class ProjectAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Amenity
        fields = '__all__'

# Paid Amenity Serializer
class ProjectPaidAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_PaidAmenity
        fields = '__all__'

class NearBySerializer(serializers.ModelSerializer):
    class Meta:
        model = NearBy
        fields = '__all__'

class ProjectSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSpecification
        fields = '__all__'

class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'

















# Serializer for Product Detail
# class ProductDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductDetail
#         fields = '__all__'

# # Serializer for Raise Cost
# class RaiseCostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RaiseCost
#         fields = '__all__'

# # Serializer for Product Cost
# class ProductCostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCost
#         fields = '__all__'
# from rest_framework import serializers
# from .models import ProductCost, AmenityCost

# # Serializer for Product Cost
# class ProductCost_1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCost_1
#         fields = '__all__'

# # Serializer for Amenity Cost
# class AmenityCostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AmenityCost
#         fields = '__all__'

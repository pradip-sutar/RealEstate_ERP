from rest_framework import serializers
from .models import *

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Type
        fields = '__all__'


class ProjectPaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Payment_Schedule
        fields = '__all__'

class ProjectProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Product_Type
        fields = '__all__'

class ProjectRaiseCostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_RaiseCost_Type
        fields = '__all__'

class ProjectAmenityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Amenity_Master
        fields = '__all__'

class ProjectNearbySegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Nearby_Segment
        fields = '__all__'

class ProjectFacingMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Facing_Master
        fields = '__all__'

class ProjectCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Commission
        fields = '__all__'

class ProductOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Ownership
        fields = '__all__'

class ProductApprovalBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_ApprovalBody
        fields = '__all__'

class ProjectTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Tax
        fields = '__all__'

class ProjectProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Product
        fields = '__all__'

class ProjectAddPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_add_Payment
        fields = '__all__'

class ProjectAddAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_add_Amenity
        fields = '__all__'

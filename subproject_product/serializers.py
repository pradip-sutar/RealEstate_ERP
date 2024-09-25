# serializers.py
from rest_framework import serializers
from .models import *
class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class EnquirySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquirySummary
        fields = '__all__'

class VisitSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitSummary
        fields = '__all__'

class QuoteSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteSummary
        fields = '__all__'

class EmployeeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeStatus
        fields = '__all__'

class CustomerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInformation
        fields = '__all__'

class CommissionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionDetails
        fields = '__all__'

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class CustomerDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDocument
        fields = '__all__'

class PropertyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDocument
        fields = '__all__'

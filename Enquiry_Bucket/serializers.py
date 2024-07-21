from rest_framework import serializers
from .models import *

class QuotationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation_Type
        fields = '__all__'

class VisitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit_Type
        fields = '__all__'

class CommunicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication_Type
        fields = '__all__'

class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source_Type
        fields = '__all__'

class EnquiryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry_Type
        fields = '__all__'

class LeadEnquiryStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead_Enquiry_Stage
        fields = '__all__'

class LeadEnquiryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead_Enquiry_Status
        fields = '__all__'

class CustomerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Form
        fields = '__all__'
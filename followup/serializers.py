from rest_framework import serializers
from .models import *

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class SiteVisitScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site_visit_schedule
        fields = '__all__'

    def validate_visitors(self, value):
        # Custom validation for visitors field if needed
        if not isinstance(value, list):
            raise serializers.ValidationError("Visitors field must be a list.")
        return value

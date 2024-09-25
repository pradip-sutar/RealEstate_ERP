from rest_framework import serializers
from .models import *
class PaymentReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReceipt
        fields = '__all__'


class PaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSchedule
        fields = '__all__'


class SalesAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesAgreement
        fields = '__all__'

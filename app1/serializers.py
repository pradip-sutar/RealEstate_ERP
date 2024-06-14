from rest_framework import serializers
from app1.models import *


class SystemCompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_company_type
        fields = "__all__"

class SystemCompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_company_detail
        fields = "__all__"

class SystemCompanyBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_brand_detail
        fields = "__all__"

class SystemBusinessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_business_detail
        fields = '__all__'

class SystemContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_contact_detail
        fields = '__all__'

class SystemSocialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_social_detail
        fields = '__all__'

class SystemOtherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_other_detail
        fields = '__all__'



class SystemBranchTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_branch_type
        fields = '__all__'
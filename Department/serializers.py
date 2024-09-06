from . models import *
from rest_framework import serializers


class DepartmentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Name
        fields = '__all__'

class DepartmentDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Designation
        fields = '__all__'

class DepartmentLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Label
        fields = '__all__'

class DepartmentGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Grade
        fields = '__all__'

class DepartmentRolesRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Roles_Rights
        fields = '__all__'
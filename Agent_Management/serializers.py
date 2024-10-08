from rest_framework import serializers
from .models import *


class AgentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent_type
        fields = ['id', 'department', 'agent_name']

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_profile
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Profile
        fields = '__all__'

class FamilyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyProfile
        fields = '__all__'

class EducationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationProfile
        fields = '__all__'

class TrainigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainig
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill_Level
        fields = '__all__'
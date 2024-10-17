from rest_framework import serializers
from .models import *


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'  # Include all fields or specify which ones you need

class DocumentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_History
        fields = '__all__'  # Include all fields or specify which ones you need

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'  # Include all fields or specify which ones you need

class PreProjectNewSerializer(serializers.ModelSerializer):
    # Optionally include the document uploads if needed
    class Meta:
        model = PreProjectNew
        fields = '__all__'
    
      

class ProjectSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectsegment
        fields = '__all__'

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecttype
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documenttype
        fields = '__all__'

class ApprovalBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval_body
        fields = '__all__'  # Include ID for reference if needed


# class ConfirmProjectSerializer(serializers.ModelSerializer):
#     project_id = serializers.CharField(source='project_id.project_id')  # Access project_id from PreProjectNew
#     uploads = DocumentUploadSerializer(many=True, read_only=True)
#     class Meta:
#         model = Confirm_Project
#         fields = '__all__' 
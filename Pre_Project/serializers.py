from rest_framework import serializers
from .models import *


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUpload
        fields = ['id', 'document_type','document']  # Include any other fields you want to expose

class PreProjectNewSerializer(serializers.ModelSerializer):
    # Optionally include the document uploads if needed
    uploads = DocumentUploadSerializer(many=True, read_only=True)

    class Meta:
        model = PreProjectNew
        fields = [
        'project_id', 
        'project_city', 
        'ownership_type', 
        'project_segments', 
        'project_name', 
        'project_types',
        'project_address',
        'longitude',
        'latitude',
        'project_measurement',
        'project_description', 
        'project_area', 
        'approvals', 
        'expenses', 
        'document_history',
        'uploads'# Include if you want to show uploaded documents in the response
        ]

    def create(self, validated_data):
        # Extract uploads data
        approval_documents = self.context['request'].FILES.getlist('Approval_document')
        history_documents = self.context['request'].FILES.getlist('History_document')
        Agreement_document=self.context['request'].FILES.getlist('Agreement_document')

        # Create the PreProject instance
        preproject = PreProjectNew.objects.create(**validated_data)

        # Save each uploaded approval document
        for upload in approval_documents:
            DocumentUpload.objects.create(pre_project=preproject, document=upload, document_type='approvals')

        # Save each uploaded history document
        for upload in history_documents:
            DocumentUpload.objects.create(pre_project=preproject, document=upload, document_type='history')

        # Save each uploaded Agreement document
        for upload in Agreement_document:
            DocumentUpload.objects.create(pre_project=preproject, document=upload, document_type='agreement')

        return preproject
    
      

class ProjectSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectsegment
        fields = ['id', 'name']

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecttype
        fields = ['id', 'name']

class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documenttype
        fields = ['id', 'name']

class ApprovalBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval_body
        fields = ['id', 'name']  # Include ID for reference if needed


class ConfirmProjectSerializer(serializers.ModelSerializer):
    project_id = serializers.CharField(source='project_id.project_id')  # Access project_id from PreProjectNew
    uploads = DocumentUploadSerializer(many=True, read_only=True)
    class Meta:
        model = Confirm_Project
        fields = '__all__' 
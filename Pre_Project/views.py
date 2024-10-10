from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db import transaction
from . models import *
from django.http import JsonResponse
from . serializers import *
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
@transaction.atomic
def pre_project_new_handler(request):
    try:
        if request.method == 'GET':
            id = request.query_params.get('id',None)
            if id:
                project = PreProjectNew.objects.get(id=id)
                serializer = PreProjectNewSerializer(project)
                return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                projects = PreProjectNew.objects.all()
                serializer = PreProjectNewSerializer(projects, many=True)
                return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)
                
     
        if request.method == 'POST':
            # Create a serializer instance with the request context
            serializer = PreProjectNewSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()  # Save the project and associated uploads
                return JsonResponse({"message": "Pre-Project created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
@transaction.atomic
def delete_pre_project_handler(request, id=None):
    try:
        if request.method == 'POST':
            if id:
                try:
                    project = PreProjectNew.objects.get(id=id)
                    project.delete()
                    return JsonResponse({'message': 'Pre-Project deleted'}, status=status.HTTP_200_OK)
                except PreProjectNew.DoesNotExist:
                    return JsonResponse({'error': 'Pre-Project not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
def transfer_to_confirm_project(request):
    if request.method == 'POST':
        try:
            pre_project = PreProjectNew.objects.get(project_id=request.data.get('project_id'))
            
            # Log for debugging
            print("PreProjectNew Found:", pre_project)

            # Create Confirm_Project instance with the PreProjectNew reference
            confirm_project = Confirm_Project.objects.create(
                project_id=pre_project,  # Set project_id to the PreProjectNew instance
                project_city=request.data.get('project_city'),
                ownership_type=request.data.get('ownership_type'),
                project_segments=request.data.get('project_segments'),  # Ensure this is in correct format
                project_name=request.data.get('project_name'),
                project_types=request.data.get('project_types'),
                project_address=request.data.get('project_address'),
                longitude=request.data.get('longitude'),
                latitude=request.data.get('latitude'),
                project_measurement=request.data.get('project_measurement'),
                project_description=request.data.get('project_description'),
                project_area=request.data.get('project_area'),
                approvals=request.data.get('approvals'),
                expenses=request.data.get('expenses'),
                document_history=request.data.get('document_history'),
            )

            # Handle uploads (assuming files are uploaded separately)
            uploads = request.FILES.getlist('uploads')
            uploads_data = []

            for file in uploads:
                document_upload = DocumentUpload.objects.create(
                    pre_project=pre_project,  # Reference to PreProjectNew
                    document=file,
                    approval_body=None,  # Assign this appropriately if needed
                )
                uploads_data.append(document_upload)

            # Add uploads to the Confirm_Project instance
            confirm_project.uploads.set(uploads_data)
            confirm_project.save()

            # Optionally, delete the PreProjectNew instance after transfer
            pre_project.delete()

            return JsonResponse(
                {'message': 'Project transferred to ConfirmProject and deleted from PreProjectNew successfully'},
                status=status.HTTP_201_CREATED
            )

        except PreProjectNew.DoesNotExist:
            return JsonResponse({'error': 'Pre-Project not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
@transaction.atomic
def delete_confirm_project_handler(request, id=None):
    try:
        if request.method == 'POST':
            if id:
                try:
                    project = Confirm_Project.objects.get(id=id)
                    project.delete()
                    return Response({'message': 'Confirm Project deleted'}, status=status.HTTP_200_OK)
                except Confirm_Project.DoesNotExist:
                    return Response({'error': 'Confirm Project not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

#========================================== Master views ============================================#

from rest_framework.response import Response


@api_view(['GET', 'POST'])
def project_segment_list(request):
    if request.method == 'GET':
        segments = Projectsegment.objects.all()
        serializer = ProjectSegmentSerializer(segments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSegmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def project_type_list(request):
    if request.method == 'GET':
        project_types = Projecttype.objects.all()
        serializer = ProjectTypeSerializer(project_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def document_type_list(request):
    if request.method == 'GET':
        document_types = Documenttype.objects.all()
        serializer = DocumentTypeSerializer(document_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocumentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def approval_body_view(request, pk=None):
    """
    Handle listing, creating, retrieving, updating, and deleting ApprovalBody instances.
    """
    if request.method == 'GET':
        # If pk is provided, retrieve a specific instance
        if pk:
            try:
                approval_body = Approval_body.objects.get(pk=pk)
                serializer = ApprovalBodySerializer(approval_body)
                return Response(serializer.data)
            except Approval_body.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # Otherwise, return a list of all instances
        approval_bodies = Approval_body.objects.all()
        serializer = ApprovalBodySerializer(approval_bodies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new ApprovalBody instance
        serializer = ApprovalBodySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # Update an existing ApprovalBody instance
        if pk:
            try:
                approval_body = Approval_body.objects.get(pk=pk)
                serializer = ApprovalBodySerializer(approval_body, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Approval_body.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a specific ApprovalBody instance
        if pk:
            try:
                approval_body = Approval_body.objects.get(pk=pk)
                approval_body.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Approval_body.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
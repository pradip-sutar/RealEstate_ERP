from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db import transaction
from . models import *
from django.http import JsonResponse
from . serializers import *
from rest_framework import status
import json
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@transaction.atomic
def pre_project_new_handler(request):
    try:
        if request.method == 'GET':
            project_id = request.query_params.get('project_id', None)

            if project_id:
                try:
                    # Fetch project by project_id
                    project = PreProjectNew.objects.get(project_id=project_id)
                    serializer = PreProjectNewSerializer(project)
                    return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

                except PreProjectNew.DoesNotExist:
                    # Return a response if project_id doesn't exist
                    return JsonResponse(
                        {"error": f"Pre-Project with project_id '{project_id}' does not exist."},
                        status=status.HTTP_404_NOT_FOUND
                    )
            else:
                # Return all projects if no specific project_id is provided
                projects = PreProjectNew.objects.all()
                serializer = PreProjectNewSerializer(projects, many=True)
                return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            # Create a serializer instance with the request context
            serializer = PreProjectNewSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()  # Save the project and associated uploads
                return JsonResponse({"message": "Pre-Project created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            project_id = request.query_params.get('project_id', None)
            if project_id:
                try:
                    # Fetch the project to be updated
                    project = PreProjectNew.objects.get(project_id=project_id)
                    serializer = PreProjectNewSerializer(project, data=request.data, partial=True, context={'request': request})

                    if serializer.is_valid():
                        serializer.save()  # Save the updated project
                        return JsonResponse({"message": "Pre-Project updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except PreProjectNew.DoesNotExist:
                    return JsonResponse(
                        {"error": f"Pre-Project with project_id '{project_id}' does not exist."},
                        status=status.HTTP_404_NOT_FOUND
                    )
            else:
                return JsonResponse({"error": "project_id must be provided for updating."}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            project_id = request.query_params.get('project_id', None)
            if project_id:
                try:
                    # Delete the project by project_id
                    project = PreProjectNew.objects.get(project_id=project_id)
                    project.delete()
                    return JsonResponse({"message": "Pre-Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
                except PreProjectNew.DoesNotExist:
                    return JsonResponse(
                        {"error": f"Pre-Project with project_id '{project_id}' does not exist."},
                        status=status.HTTP_404_NOT_FOUND
                    )
            else:
                return JsonResponse({"error": "project_id must be provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # Return a 500 error for any unexpected errors
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


# @api_view(['POST'])
# @transaction.atomic
# def delete_pre_project_handler(request, id=None):
#     try:
#         if request.method == 'POST':
#             if id:
#                 try:
#                     project = PreProjectNew.objects.get(id=id)
#                     project.delete()
#                     return JsonResponse({'message': 'Pre-Project deleted'}, status=status.HTTP_200_OK)
#                 except PreProjectNew.DoesNotExist:
#                     return JsonResponse({'error': 'Pre-Project not found'}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 return JsonResponse({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['GET', 'POST', 'DELETE'])
@transaction.atomic
def confirm_project_handler(request, project_id=None):
    try:
        if request.method == 'POST':
            # print(request.data)
            if request.content_type.startswith('multipart/form-data'):
                data = request.POST
            elif request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                return JsonResponse({'error': 'Unsupported Content-Type'}, status=status.HTTP_400_BAD_REQUEST)
            # Handle POST request - Transfer PreProjectNew to Confirm_Project

            project_id = data.get('project_id')
            if not project_id:
                return JsonResponse({'error': 'project_id is required'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                pre_project = PreProjectNew.objects.get(project_id=request.data.get('project_id'))
                
                # Create Confirm_Project instance with the PreProjectNew reference
                confirm_project = Confirm_Project.objects.create(
                    project_id=pre_project.project_id,  # Set project_id to the PreProjectNew instance
                    project_city=request.data.get('project_city'),
                    ownership_type=request.data.get('ownership_type'),
                    project_segments=request.data.get('project_segments'),
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
                # print(confirm_project)
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

        elif request.method == 'GET':
            # Handle GET request - Fetch Confirm_Project by query parameters
            try:
                project_id = request.query_params.get('project_id', None)
                project_city = request.query_params.get('project_city', None)
                
                # You can filter based on these fields
                filters = {}
                if project_id:
                    filters['project_id'] = project_id
                if project_city:
                    filters['project_city'] = project_city

                # Fetch all projects matching the filters
                projects = Confirm_Project.objects.filter(**filters)

                if not projects.exists():
                    return JsonResponse({'message': 'No projects found'}, status=status.HTTP_404_NOT_FOUND)

                # Prepare the response data
                project_data = []
                for project in projects:
                    # Include the uploaded document URLs
                    uploads = [
                        {
                            "file_name": upload.document.name,  # Filename of the document
                            "file_url": upload.document.url    # URL to access the document
                        }
                        for upload in project.uploads.all()
                    ]
                    
                    project_data.append({
                        'project_id': project.project_id,
                        'project_city': project.project_city,
                        'ownership_type': project.ownership_type,
                        'project_segments': project.project_segments,
                        'project_name': project.project_name,
                        'project_types': project.project_types,
                        'project_address': project.project_address,
                        'longitude': project.longitude,
                        'latitude': project.latitude,
                        'project_measurement': project.project_measurement,
                        'project_description': project.project_description,
                        'project_area': project.project_area,
                        'approvals': project.approvals,
                        'expenses': project.expenses,
                        'document_history': project.document_history,
                        'uploads': uploads  # Add uploads (file URLs)
                    })

                return JsonResponse({'projects': project_data}, status=status.HTTP_200_OK, safe=False)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        elif request.method == 'DELETE':
            # Handle DELETE request - Delete Confirm_Project
            project_id = request.query_params.get('project_id', None)  # Get project_id from query params

            if project_id is not None:
                try:
                    # Get the Confirm_Project instance by project_id
                    confirm_project = Confirm_Project.objects.get(project_id=project_id)
                    
                    # Log for debugging
                    # print(f"Deleting Confirm_Project: {confirm_project.project_name}")
                    
                    # Delete the project
                    confirm_project.delete()

                    return JsonResponse(
                        {"message": f"Project '{confirm_project.project_name}' deleted successfully."}, 
                        status=status.HTTP_200_OK
                    )
                
                except Confirm_Project.DoesNotExist:
                    return JsonResponse({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
                
                except Exception as e:
                    return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return JsonResponse({"error": "project_id must be provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # Return a 500 error for any unexpected errors
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

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
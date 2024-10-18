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
                # Fetch a single project by project_id
                try:
                    project = PreProjectNew.objects.get(project_id=project_id)
                    project_serializer = PreProjectNewSerializer(project)

                    # Fetch related data (approvals, documents, agreements) linked to the project
                    approvals = Approval.objects.filter(preproject=project)
                    approvals_serializer = ApprovalBodySerializer(approvals, many=True)

                    document_history = Document_History.objects.filter(preproject=project)
                    document_serializer = DocumentHistorySerializer(document_history, many=True)

                    agreements = Agreement.objects.filter(preproject=project)
                    agreement_serializer = AgreementSerializer(agreements, many=True)

                    # Combine the project and related data
                    data = {
                        "preproject": project_serializer.data,
                        "approvals": approvals_serializer.data,
                        "document_history": document_serializer.data,
                        "agreement": agreement_serializer.data,
                    }
                    return JsonResponse({"data": data}, status=status.HTTP_200_OK)

                except PreProjectNew.DoesNotExist:
                    return JsonResponse(
                        {"error": f"Pre-Project with project_id '{project_id}' does not exist."},
                        status=status.HTTP_404_NOT_FOUND
                    )

            else:
                # Fetch all projects
                preprojects = PreProjectNew.objects.all()

                # Create a list to hold all projects with their related data
                all_projects_data = []

                for project in preprojects:
                    # Serialize each project
                    project_serializer = PreProjectNewSerializer(project)

                    # Fetch related data for the current project
                    approvals = Approval.objects.filter(preproject=project)
                    approvals_serializer = ApprovalSerializer(approvals, many=True)

                    document_history = Document_History.objects.filter(preproject=project)
                    document_serializer = DocumentHistorySerializer(document_history, many=True)

                    agreements = Agreement.objects.filter(preproject=project)
                    agreement_serializer = AgreementSerializer(agreements, many=True)

                    # Construct a dictionary for the current project with all its related data
                    project_data = {
                        "preproject": project_serializer.data,
                        "approvals": approvals_serializer.data,
                        "document_history": document_serializer.data,
                        "agreement": agreement_serializer.data,
                    }

                    # Append this project's data to the list
                    all_projects_data.append(project_data)

                # Return the list of all projects with their related data
                return JsonResponse({"data": all_projects_data}, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            print(request.data)
            try:
                with transaction.atomic():
                    def organize_list_data(data, prefix):
                        """Organize nested list-like data with dot notation."""
                        list_data = []
                        index = 0
                        while True:
                            entry_data = {}
                            found = False
                            for key, value in data.items():
                                # Check if the key starts with the prefix and has the dot notation
                                if key.startswith(f'{prefix}[{index}].'):
                                    field_name = key.split('.')[1]  # Extract the field name after the dot
                                    entry_data[field_name] = value
                                    found = True
                            if not found:
                                break
                            list_data.append(entry_data)
                            index += 1
                        return list_data
                    
                    document_history = organize_list_data(request.data, 'document_history')
                    approval_body = organize_list_data(request.data, 'approval_body')
                    agreement = organize_list_data(request.data, 'agreement')
                    # Create a serializer instance with the request context

                    PreProjectSerializer = PreProjectNewSerializer(data=request.data)
                    if PreProjectSerializer.is_valid():
                        pre_project = PreProjectSerializer.save()  # Save the project and associated uploads
                    else:
                        return JsonResponse(PreProjectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    # add the preproject id into the other models
                    
                    for approval in approval_body:
                        approval['preproject']=pre_project.project_id
                        approvalSerializer = ApprovalSerializer(data = approval)
                        if approvalSerializer.is_valid():
                            approvalSerializer.save()  # Save the approval
                        else:
                            return JsonResponse(approvalSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                    for document in document_history:
                        document['preproject']=pre_project.project_id
                        documentSerializer = DocumentHistorySerializer(data = document)
                        if documentSerializer.is_valid():
                            documentSerializer.save()  # Save the approval
                        else:
                            return JsonResponse(documentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    for agreement_data in agreement:
                        agreement_data['preproject']=pre_project.project_id
                        agreementSerializer = AgreementSerializer(data = agreement_data)
                        if agreementSerializer.is_valid():
                            agreementSerializer.save()  # Save the approval
                        else:
                            return JsonResponse(agreementSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    return JsonResponse({"message": "Pre-Project created successfully"}, status=status.HTTP_201_CREATED)
                # else:
                #     return JsonResponse(PreProjectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
                    return JsonResponse({"message": "Pre-Project deleted successfully."}, status=status.HTTP_200_OK)
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
def confirm_project_handler(request):
    try:
        if request.method == 'POST':
            project_id = request.query_params.get('project_id',None)
            print(project_id)
            if not project_id:
                return JsonResponse({'error': 'project_id is required'}, status=status.HTTP_400_BAD_REQUEST)

            # try:
            pre_project = PreProjectNew.objects.get(project_id=project_id)
            # Create Confirm_Project instance with the PreProjectNew reference
            confirm_project = Confirm_Project.objects.create(
                project_id=pre_project.project_id,  # Set project_id to the PreProjectNew instance
                project_city=pre_project.project_city,
                ownership_type=pre_project.ownership_type,
                project_segments=pre_project.project_segments,
                project_name=pre_project.project_name,
                project_types=pre_project.project_types,
                project_address=pre_project.project_address,
                longitude=pre_project.longitude,
                latitude=pre_project.latitude,
                project_measurement=pre_project.project_measurement,
                project_description=pre_project.project_description,
                project_area=pre_project.project_area,
                expenses=pre_project.expenses,
            )
            # confirm_project_id = confirm_project.project_id
            approvals = Approval.objects.filter(preproject=project_id)
            for approval in approvals:
                # Serialize the data from `approval` to create a new ConfirmApproval
                approval_data = {
                    "approvalBody": approval.approvalBody,
                    "applyDate": approval.applyDate,
                    "employeeName": approval.employeeName,
                    "agency": approval.agency,
                    "approvalDate": approval.approvalDate,
                    "validityNo": approval.validityNo,
                    "document": approval.document,  # Assuming it's a file path
                    "preproject": approval.preproject.project_id  # Assuming this field is related to the preproject ID
                }
                print(approval_data)
                approval_serializer = ConfirmApprovalSerializer(data=approval_data)
                # Validate and save if valid
                if approval_serializer.is_valid():
                    approval_serializer.save()
                else:
                    print(approval_serializer.errors)  # Print any errors in validation
            
            document_histories = Document_History.objects.filter(preproject=project_id)
            for document_history in document_histories:
                print(document_history)

                # Serialize the data from `Document_History` to create a new Confirm_Document_History
                document_history_data = {
                    "documentType": document_history.documentType,
                    "documentNo": document_history.documentNo,
                    "issuedBy": document_history.issuedBy,
                    "issueDate": document_history.issueDate,
                    "validation": document_history.validation,
                    "uploadDocument": document_history.uploadDocument,  # Assuming it's a file path
                    "preproject": document_history.preproject.project_id  # Assuming this field is related to the preproject ID
                }

                document_history_serializer = ConfirmDocumentHistorySerializer(data=document_history_data)

                # Validate and save if valid
                if document_history_serializer.is_valid():
                    document_history_serializer.save()
                else:
                    print(document_history_serializer.errors)  # Print any errors in validation

            agreements = Agreement.objects.filter(preproject=project_id)
            for agreement in agreements:
                print(agreement)
                # Serialize the data from `Agreement` to create a new Confirm_Agreement
                agreement_data = {
                    "upload_document": agreement.upload_document,  # Assuming it's a file path
                    "preproject": agreement.preproject.project_id  # Assuming this field is related to the preproject ID
                }
                agreement_serializer = ConfirmAgreementSerializer(data=agreement_data)
                # Validate and save if valid
                if agreement_serializer.is_valid():
                    agreement_serializer.save()
                else:
                    print(agreement_serializer.errors)  # Print any errors in validation

            # After transfer all the data of PreProject it would delete....
            pre_project.delete()

            return JsonResponse({'message': "Confirm project created successfully"}, status=status.HTTP_201_CREATED)

        elif request.method == 'GET':
            # Handle GET request - Fetch Confirm_Project by query parameters
            try:
                project_id = request.query_params.get('project_id', None)
                
                # You can filter based on these fields
                filters = {}
                if project_id:
                    filters['project_id'] = project_id

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
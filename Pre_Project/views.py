from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db import transaction
from . models import *
from django.http import JsonResponse
from . serializers import *
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
@transaction.atomic
def pre_project_new_handler(request):
    try:
        if request.method == 'GET':
            projects = PreProjectNew.objects.all()
            serializer = PreProjectNewSerializer(projects, many=True)
            return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = PreProjectNewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Pre-Project created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET', 'POST'])
@transaction.atomic
def confirm_project_handler(request, id=None):
    try:
        if request.method == 'POST' and id:
            pre_project_data = PreProjectNew.objects.get(id=id)
            
            pre_project_serializer = PreProjectNewSerializer(pre_project_data)
            serialized_data = pre_project_serializer.data
            print(serialized_data)
            serialized_data.pop('generate_agreement', None)
            serialized_data.pop('upload_document', None)

            confirm_project_serializer = ConfirmProjectSerializer(data=serialized_data)
            
            if confirm_project_serializer.is_valid():
                confirm_project_instance = confirm_project_serializer.save()

                confirm_project_instance.generate_agreement = pre_project_data.generate_agreement
                confirm_project_instance.upload_document = pre_project_data.upload_document
                confirm_project_instance.save()

                pre_project_data.delete()
                
                return JsonResponse(confirm_project_serializer.data, safe=False)
            return JsonResponse(confirm_project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'GET' and id:
            pre_project_data = PreProjectNew.objects.get(id=id)
            serializer = PreProjectNewSerializer(pre_project_data)
            return JsonResponse(serializer.data, safe=False)
        
    except PreProjectNew.DoesNotExist:
        return JsonResponse({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
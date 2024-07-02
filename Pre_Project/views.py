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
from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import transaction
import random
from django.http import JsonResponse

# Create your views here.
@api_view(['GET', 'POST'])
@transaction.atomic
def department_name_handler(request):
    if request.method == 'GET':
        data = Department_Name.objects.all()
        serializers = DepartmentNameSerializer(data, many=True)
        return JsonResponse({"data": serializers.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        try:
            while True:
                id = random.randrange(1000000, 99999999)
                if not Department_Name.objects.filter(id=id).exists():
                    data['id'] = id
                    serializers = DepartmentNameSerializer(data=data)
                    if serializers.is_valid():
                        serializers.save()
                        return JsonResponse({"message": "Department created successfully", "data": serializers.data}, status=status.HTTP_201_CREATED)
                    else:
                        return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['GET', 'POST'])
@transaction.atomic
def department_designation_handler(request):
    if request.method == 'GET':
        data = Department_Designation.objects.all()
        serializers = DepartmentDesignationSerializer(data, many=True)
        return JsonResponse({"data": serializers.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        try:
            # Check if the designation already exists within the same department
            if Department_Designation.objects.filter(designation=data.get('designation'), dept_name=data.get('dept_name')).exists():
                return JsonResponse({"error": "Designation already exists in this department"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializers = DepartmentDesignationSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({"message": "Designation created successfully", "data": serializers.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def department_label_handler(request):
    if request.method == 'GET':
        labels = Department_Label.objects.all()
        serializer = DepartmentLabelSerializer(labels, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        serializer = DepartmentLabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def department_grade_handler(request):
    if request.method == 'GET':
        grades = Department_Grade.objects.all()
        serializer = DepartmentGradeSerializer(grades, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        serializer = DepartmentGradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
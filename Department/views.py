from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import transaction
import random
from django.http import JsonResponse

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
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
                    break
            
            serializer = DepartmentNameSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Department created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        data = request.data
        try:
            department = Department_Name.objects.get(id=data.get('id'))
            serializer = DepartmentNameSerializer(department, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Department updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department_Name.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
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

    elif request.method in ['PUT', 'PATCH']:
        data = request.data
        designation_id = data.get('id')  # Assuming the designation ID is passed in the request body

        try:
            designation_instance = Department_Designation.objects.get(id=designation_id)
            if 'designation' in data and Department_Designation.objects.filter(
                designation=data.get('designation'), 
                dept_name=data.get('dept_name')
            ).exclude(id=designation_id).exists():
                return JsonResponse({"error": "Designation already exists in this department"}, status=status.HTTP_400_BAD_REQUEST)

            serializers = DepartmentDesignationSerializer(designation_instance, data=data, partial=(request.method == 'PATCH'))
            
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({"message": "Designation updated successfully", "data": serializers.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department_Designation.DoesNotExist:
            return JsonResponse({"error": "Designation not found"}, status=status.HTTP_404_NOT_FOUND)
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
    
@api_view(['GET', 'POST'])
def department_role_rights_handler(request):
    if request.method == 'GET':
        department_roles = Department_Roles_Rights.objects.all()
        serializer = DepartmentRolesRightsSerializer(department_roles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = request.data.get('departmentRoles', {})
        department_id = department_data.get('department_id')
        roles = department_data.get('roles', [])
        print(roles)
        try:
            department_instance = Department_Name.objects.get(id=department_id)
            print(department_instance.id)
            
            for role in roles:
                role_id = role.get('roleId')
                role_instance = Roles.objects.get(id=role_id)
                
                # Fetch rights for the role
                get_rights = Rights.objects.filter(roles_id=role_instance).latest('id')
                
                # Collect the rights data
                rights_data = {
                    'view': get_rights.view,
                    'write': get_rights.write,
                    'edit': get_rights.edit,
                    'delete': get_rights.delete
                }
                
                # Create Department_Roles_Rights and assign role_name explicitly
                Department_Roles_Rights.objects.create(
                    role_id=role_instance, 
                    role_name=role_instance.name,  # Assuming role_instance has a 'name' field
                    department_id=department_instance,
                    **rights_data
                )
                print("All rights: ", rights_data)
                
        except Department_Name.DoesNotExist:
            return JsonResponse({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)
        except Roles.DoesNotExist:
            return JsonResponse({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return JsonResponse({"message": "Roles and rights saved/updated successfully."}, status=status.HTTP_201_CREATED)


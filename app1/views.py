from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from app1.models import *
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.db import transaction, IntegrityError
import re
import random
# Create your views here.
@csrf_exempt
def admin_view(request,mob):
    if request.method == 'GET':
        # parse = JSONParser().parse(request)
        # mob = parse.get('mobileno')
        data = Admin.objects.filter(mob=mob)
        final_data = [(i.name,i.mob,i.designation,i.department, i.designation,i.email) for i in data]
        return JsonResponse({"data":final_data})
    
@csrf_exempt
def admin_login(request):
    try:
        if request.method == 'POST':
            parse = JSONParser().parse(request)
            mob_email = parse.get('mobile_email')
            password = parse.get('password')

            if re.search(r".*com$", mob_email):
                data = Admin.objects.filter(email=mob_email, password=password)
            elif re.match(r"\d{10}$", mob_email):
                data = Admin.objects.filter(mob=mob_email, password=password)
            else:
                return JsonResponse({"message": "Invalid email/mobile format"}, status=400)
            if data.exists():
                final_data = [(i.name, i.mob, i.designation, i.department, i.email, i.token) for i in data]
                return JsonResponse({"message": "Login successful", "data": final_data})
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=400)
        else:
            return JsonResponse({"message": "Only POST requests are allowed"}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

@csrf_exempt
@transaction.atomic
def create_emp_profile(request):
    if request.method == 'POST':
        try:
            empid = request.POST.get('empid')
            name = request.POST.get('name')
            mobileno = request.POST.get('mobileno')
            whatsapp = request.POST.get('whatsapp')
            email = request.POST.get('email')
            emergency_no = request.POST.get('emergency_no')
            date_of_joining = request.POST.get('date_of_joining')
            date_of_leaving = request.POST.get('date_of_leaving')
            branch = request.POST.get('branch')
            department_id = request.POST.get('department_id')
            designation = request.POST.get('designation')
            level = request.POST.get('level')
            grade = request.POST.get('grade')
            role = request.POST.get('role')

            # Validate required fields
            if not all([empid, name, mobileno, email, emergency_no, date_of_joining, branch, department_id, designation, level, grade, role]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            department = get_object_or_404(Department_Name, pk=department_id)

            emp_profile = Emp_company_profile(
                empid=empid,
                name=name,
                mobileno=mobileno,
                whatsapp=whatsapp,
                email=email,
                emergency_no=emergency_no,
                date_of_joining=date_of_joining,
                date_of_leaving=date_of_leaving,
                branch=branch,
                department=department,
                designation=designation,
                level=level,
                grade=grade,
                role=role
            )

            # Save the employee profile
            emp_profile.save()
            return JsonResponse({"message": "Employee profile created successfully"}, status=201)

        except Department_Name.DoesNotExist:
            return JsonResponse({"error": "Department does not exist"}, status=400)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)

    return HttpResponse(status=405)


@csrf_exempt
@transaction.atomic
def department_name_handler(request, departmentid=None):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            name = data.get('name')
            status = data.get('status')

            # Validate required fields
            if not all([name, status is not None]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            # Check if the department name is already taken
            if Department_Name.objects.filter(name=name).exists():
                return JsonResponse({"error": "Department name already taken, please choose a different name"}, status=400)

            # Generate a unique department ID
            while True:
                departmentid = random.randint(1, 10**10)
                if not Department_Name.objects.filter(departmentid=departmentid).exists():
                    break

            department = Department_Name(departmentid=departmentid, name=name, status=status)
            department.save()
            
            return JsonResponse({"message": "Department created successfully", "departmentid": departmentid}, status=201)
        
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    elif request.method == 'GET':
        if departmentid is None:
            return JsonResponse({"error": "Department ID is required for GET requests"}, status=400)
        
        try:
            department = get_object_or_404(Department_Name, pk=departmentid)
            data = {
                "departmentid": department.departmentid,
                "name": department.name,
                "status": department.status
            }
            return JsonResponse(data, status=200)
        
        except Department_Name.DoesNotExist:
            return JsonResponse({"error": "Department does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    return HttpResponse(status=405)

@csrf_exempt
@transaction.atomic
def department_label_handler(request, labelid=None):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            designation_id = data.get('designation_id')
            label_description = data.get('label_description')
            status = data.get('status')
            print(designation_id,label_description,status)

            # Validate required fields
            if not all([designation_id, label_description]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            designation = get_object_or_404(Department_Designation, pk=designation_id)

            label_obj = Department_Label(designation=designation, label_description=label_description, status=status)
            label_obj.save()
            
            return JsonResponse({"message": "Label created successfully"}, status=201)
        
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    elif request.method == 'GET':
        if labelid is None:
            return JsonResponse({"error": "Label ID is required for GET requests"}, status=400)
        
        try:
            label_obj = get_object_or_404(Department_Label, pk=labelid)
            data = {
                "designation": label_obj.designation.designation,
                "label_description": label_obj.label_description,
                "status": label_obj.status
            }
            return JsonResponse(data, status=200)
        
        except Department_Label.DoesNotExist:
            return JsonResponse({"error": "Label does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    return HttpResponse(status=405)

@csrf_exempt
@transaction.atomic
def department_grade_handler(request, gradeid=None):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            label_id = data.get('label_id')
            grade_description = data.get('grade_description')
            status = data.get('status')

            # Validate required fields
            if not all([label_id, grade_description, status]):
                return JsonResponse({"error": "Missing required fields"}, status=400)

            label = get_object_or_404(Department_Label, pk=label_id)

            grade_obj = Department_Grade(label=label, grade_description=grade_description, status=status)
            grade_obj.save()
            
            return JsonResponse({"message": "Grade created successfully"}, status=201)
        
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    elif request.method == 'GET':
        if gradeid is None:
            return JsonResponse({"error": "Grade ID is required for GET requests"}, status=400)
        
        try:
            grade_obj = get_object_or_404(Department_Grade, pk=gradeid)
            data = {
                "label": grade_obj.label.label_description,
                "grade_description": grade_obj.grade_description,
                "status": grade_obj.status
            }
            return JsonResponse(data, status=200)
        
        except Department_Grade.DoesNotExist:
            return JsonResponse({"error": "Grade does not exist"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "An error occurred: " + str(e)}, status=500)
    
    return HttpResponse(status=405)
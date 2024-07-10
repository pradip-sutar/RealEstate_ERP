from app1.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from Department.models import *
from Employee_Management.models import *
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.db import transaction, IntegrityError
import re
import random
from rest_framework import status

# Create your views here.
@csrf_exempt
def admin_view(request,mob):
    if request.method == 'GET':
        # parse = JSONParser().parse(request)
        # mob = parse.get('mobileno')
        data = Admin.objects.filter(mob=mob)
        final_data = [(i.name,i.mob,i.designation,i.department, i.designation,i.email) for i in data]
        return JsonResponse({"data":final_data})
    
# @csrf_exempt
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

            emp_profile = Company_profile(
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


@api_view(['POST','GET','DELETE'])
@transaction.atomic
def system_company_details_handler(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        # Extract Company Detail
        company_data = {}
        for key, value in data.items():
            if key.startswith('company_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'company_detail.'
                company_data[sub_key] = value
        
        # Save Company Detail
        company_serializer = SystemCompanyDetailsSerializer(data=company_data)
        if company_serializer.is_valid():
            company_detail = company_serializer.save()
        else:
            return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #Extract Brand Detail
        brand_data = {}
        for key, value in data.items():
            if key.startswith('brand_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'brand_detail.'
                brand_data[sub_key] = value
        brand_data['company_id'] = company_detail.companyid
        
        # Save Brand Detail
        brand_serializer = SystemCompanyBrandSerializer(data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
        else:
            return JsonResponse(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract Business Detail
        business_data = {}
        for key, value in data.items():
            if key.startswith('business_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'business_detail.'
                business_data[sub_key] = value
        business_data['company_id'] = company_detail.companyid
        
        # Save Business Detail
        business_serializer = SystemBusinessDetailSerializer(data=business_data)
        if business_serializer.is_valid():
            business_serializer.save()
        else:
            return JsonResponse(business_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract Contact Detail
        contact_data = {}
        for key, value in data.items():
            if key.startswith('contact_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'contact_detail.'
                contact_data[sub_key] = value
        contact_data['company_id'] = company_detail.companyid
        
        # Save Contact Detail
        contact_serializer = SystemContactDetailSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
        else:
            return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #Extract Social Detail
        social_data={}
        for key, value in data.items():
            if key.startswith('social_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'contact_detail.'
                social_data[sub_key] = value
        social_data['company_id'] = company_detail.companyid
        
        # Save Contact Detail
        social_serializer = SystemSocialDetailSerializer(data=social_data)
        if social_serializer.is_valid():
            social_serializer.save()
        else:
            return JsonResponse(social_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     # Extract Other Detail
        other_data = {}
        for key, value in data.items():
            if key.startswith('other_detail'):
                sub_key = key.split('.', 1)[1]  # Get everything after 'contact_detail.'
                other_data[sub_key] = value
        other_data['company_id'] = company_detail.companyid
        
        # Save Other Detail
        other_serializer = SystemOtherDetailSerializer(data=other_data)
        if other_serializer.is_valid():
            other_serializer.save()
        else:
            return JsonResponse(other_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'message': 'All details saved successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST', 'GET'])
@transaction.atomic
def system_branch_type_handler(request):
    if request.method == 'POST':
        data = request.data
        serializer = SystemBranchTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Branch type saved", "data": serializer.data}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'GET':
        branch_types = System_branch_type.objects.all()
        serializer = SystemBranchTypeSerializer(branch_types, many=True)
        return JsonResponse({"data": serializer.data}, status=200)
    

@api_view(['POST', 'GET'])
@transaction.atomic
def system_branch_handler(request):
    if request.method == 'POST':
        data = request.data

        # Save branch details
        branch_details_data = data.get('branch_details', {})
        branch_details_serializer = SystemBranchDetailsSerializer(data=branch_details_data)
        if branch_details_serializer.is_valid():
            branch_details = branch_details_serializer.save()
        else:
            return JsonResponse(branch_details_serializer.errors, status=400)

        # Save branch brand
        branch_brand_data = data.get('branch_brand', {})
        branch_brand_data['branch'] = branch_details.branch_id
        branch_brand_serializer = SystemBranchBrandSerializer(data=branch_brand_data)
        if branch_brand_serializer.is_valid():
            branch_brand_serializer.save()
        else:
            return JsonResponse(branch_brand_serializer.errors, status=400)

        # Save branch contact
        branch_contact_data = data.get('branch_contact', {})
        branch_contact_data['branch'] = branch_details.branch_id
        branch_contact_serializer = SystemBranchContactSerializer(data=branch_contact_data)
        if branch_contact_serializer.is_valid():
            branch_contact_serializer.save()
        else:
            return JsonResponse(branch_contact_serializer.errors, status=400)

        return JsonResponse({"message": "Branch details, brand, and contact saved successfully"}, status=201)

    elif request.method == 'GET':
        branch_id = request.query_params.get('branch_id', None)
        if branch_id is not None:
            try:
                branch_id = int(branch_id)
            except ValueError:
                return JsonResponse({"error": "Invalid branch_id"}, status=400)

            # Retrieve branch details
            try:
                branch_details = System_branch_details.objects.get(branch_id=branch_id)
                branch_details_serializer = SystemBranchDetailsSerializer(branch_details)
            except System_branch_details.DoesNotExist:
                return JsonResponse({"error": "Branch details not found"}, status=404)

            # Retrieve branch brand
            try:
                branch_brand = System_branch_brand.objects.get(branch=branch_details)
                branch_brand_serializer = SystemBranchBrandSerializer(branch_brand)
            except System_branch_brand.DoesNotExist:
                branch_brand_serializer = None

            # Retrieve branch contact
            try:
                branch_contact = System_branch_contact.objects.get(branch=branch_details)
                branch_contact_serializer = SystemBranchContactSerializer(branch_contact)
            except System_branch_contact.DoesNotExist:
                branch_contact_serializer = None

            data = {
                "branch_details": branch_details_serializer.data,
                "branch_brand": branch_brand_serializer.data if branch_brand_serializer else None,
                "branch_contact": branch_contact_serializer.data if branch_contact_serializer else None
            }
            return JsonResponse({"data": data}, status=200)

        else:
            # Retrieve all branch details
            branch_details = System_branch_details.objects.all()
            branch_details_serializer = SystemBranchDetailsSerializer(branch_details, many=True)
            branch_brands = System_branch_brand.objects.all()
            branch_brand_serializer = SystemBranchBrandSerializer(branch_brands, many=True)
            branch_contacts = System_branch_contact.objects.all()
            branch_contact_serializer = SystemBranchContactSerializer(branch_contacts, many=True)

            data = {
                "branch_details": branch_details_serializer.data,
                "branch_brands": branch_brand_serializer.data,
                "branch_contacts": branch_contact_serializer.data
            }
            return JsonResponse({"data": data}, status=200)
        
@api_view(['POST', 'GET'])
@transaction.atomic
def system_bank_details_handler(request):
    if request.method == 'POST':
        data = request.data
        serializer = SystemBankDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Bank details saved", "data": serializer.data}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'GET':
        bank_name = request.query_params.get('bank_name', None)
        branch_name = request.query_params.get('branch_name', None)
        
        filters = {}
        if bank_name:
            filters['bank_name__icontains'] = bank_name
        if branch_name:
            filters['branch_name__icontains'] = branch_name

        bank_details = System_bank_details.objects.filter(**filters)
        serializer = SystemBankDetailsSerializer(bank_details, many=True)
        return JsonResponse({"data": serializer.data}, status=200)
    
@api_view(['GET', 'POST'])
def system_board_of_directors_handler(request):
    if request.method == 'POST':
        serializer = SystemBoardOfDirectorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        directors = System_Board_of_Directors.objects.all()
        serializer = SystemBoardOfDirectorsSerializer(directors, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET', 'POST'])
@transaction.atomic
def customer_handler(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({"data": serializer.data}, status=200)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Customer created successfully", "data": serializer.data}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    

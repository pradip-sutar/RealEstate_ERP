from System_Admin.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from Department.models import *
from Employee_Management.models import *
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.db import transaction, IntegrityError
import re
import random
from rest_framework import status

# Create your views here.


@csrf_exempt
def admin_view(request, mob):
    if request.method == 'GET':
        # parse = JSONParser().parse(request)
        # mob = parse.get('mobileno')
        data = Admin.objects.filter(mob=mob)
        final_data = [(i.name, i.mob, i.designation, i.department,
                       i.designation, i.email) for i in data]
        return JsonResponse({"data": final_data})

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
                final_data = [(i.name, i.mob, i.designation,
                               i.department, i.email, i.token) for i in data]
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


@api_view(['POST', 'GET', 'DELETE'])
@transaction.atomic
def system_company_details_handler(request):
    if request.method == 'POST':
        print(request.data)
        
        # Helper function to split and organize the data by prefix
        def organize_data(data, prefix):
            prefix_data = {}
            for key, value in data.items():
                if key.startswith(prefix):
                    field_name = key.split('[')[1][:-1]  # Extract the field inside the brackets
                    prefix_data[field_name] = value  # Assuming value is in list form like ['100']
            return prefix_data
        
        def organize_list_data(data, prefix):
            """Organize nested list-like data."""
            list_data = []
            index = 0
            while True:
                entry_data = {}
                found = False
                for key, value in data.items():
                    if key.startswith(f'{prefix}[{index}]'):
                        field_name = key.split('[')[2][:-1]  # Extract field name
                        entry_data[field_name] = value
                        found = True
                if not found:
                    break
                list_data.append(entry_data)
                index += 1
            return list_data

        # Extract and organize the data based on the prefix
        company_data = organize_data(request.data, 'company_detail')
        print("company data ..................", company_data)
        brand_data = organize_data(request.data, 'brand_detail')
        print("brand data ..................", brand_data)
        business_data = organize_data(request.data, 'business_detail')
        print("business data ..................", business_data)
        contact_data = organize_data(request.data, 'contact_detail')
        print("contact data ..................", contact_data)

        # For lists like social_detail and other_detail, we use the new organize_list_data function
        social_data_list = organize_list_data(request.data, 'social_detail')
        print("social data ..................", social_data_list)
        other_data_list = organize_list_data(request.data, 'other_detail')
        print("other data ..................", other_data_list)

        try:
            # Save Company Detail
            company_serializer = SystemCompanyDetailsSerializer(data=company_data)
            if company_serializer.is_valid():
                company_instance = company_serializer.save()  # Save and get the instance
            else:
                return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Attach company_id to the related details before saving them
            brand_data['company_id'] = company_instance.companyid
            business_data['company_id'] = company_instance.companyid
            contact_data['company_id'] = company_instance.companyid

            # Save Brand Detail
            brand_serializer = SystemCompanyBrandSerializer(data=brand_data)
            if brand_serializer.is_valid():
                brand_serializer.save()
            else:
                return JsonResponse(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save Business Detail
            business_serializer = SystemBusinessDetailSerializer(data=business_data)
            if business_serializer.is_valid():
                business_serializer.save()
            else:
                return JsonResponse(business_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save Contact Detail
            contact_serializer = SystemContactDetailSerializer(data=contact_data)
            if contact_serializer.is_valid():
                contact_serializer.save()
            else:
                return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save each Social Detail (handling multiple entries)
            for social_data in social_data_list:
                social_data['company_id'] = company_instance.companyid
                social_serializer = SystemSocialDetailSerializer(data=social_data)
                if social_serializer.is_valid():
                    social_serializer.save()
                else:
                    return JsonResponse(social_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save each Other Detail (handling multiple entries)
            for other_data in other_data_list:
                other_data['company_id'] = company_instance.companyid
                other_serializer = SystemOtherDetailSerializer(data=other_data)
                if other_serializer.is_valid():
                    other_serializer.save()
                else:
                    return JsonResponse(other_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse({'message': 'All details saved successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        company_id = request.query_params.get('company_id', None)
        if company_id is not None:
            company_details = System_company_detail.objects.filter(companyid=company_id)
            brand_details = System_brand_detail.objects.filter(company_id=company_id)
            contact_details = System_contact_detail.objects.filter(company_id=company_id)
            business_details = System_business_detail.objects.filter(company_id=company_id)
            social_details = System_social_detail.objects.filter(company_id=company_id)
            other_details = System_other_detail.objects.filter(company_id=company_id)

            details_serializer = SystemCompanyDetailsSerializer(company_details, many=True)
            brand_serializer = SystemCompanyBrandSerializer(brand_details, many=True)
            contact_serializer = SystemContactDetailSerializer(contact_details, many=True)
            business_serializer = SystemBusinessDetailSerializer(business_details, many=True)
            social_serializer = SystemSocialDetailSerializer(social_details, many=True)
            other_serializer = SystemOtherDetailSerializer(other_details, many=True)

            return JsonResponse({
                "data": {
                    "details": details_serializer.data,
                    "brand_info": brand_serializer.data,
                    "contact_info": contact_serializer.data,
                    "business_details": business_serializer.data,
                    "social_details": social_serializer.data,
                    "other_details": other_serializer.data
                }
            }, status=200)
        else:
            company_details = System_company_detail.objects.all()
            serializer = SystemCompanyDetailsSerializer(company_details, many=True)
            return JsonResponse({"data": serializer.data}, status=200)
        
        
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
        # Extracting data for branch details
        branch_details_data = {
            'branch_name': request.data.get('branch_name'),
            'alias': request.data.get('alias'),
            'company_id': request.data.get('company_id'),  # ForeignKey
            'branch_type': request.data.get('branch_type'),  # ForeignKey
            'size': request.data.get('size'),
            'incorporation_no': request.data.get('incorporation_no'),
            'incorporation_date': request.data.get('incorporation_date'),
            'incorporation_certificate': request.FILES.get('incorporation_certificate'),  # File field
            'tax_certificate_details': request.data.get('tax_certificate_details'),
            'PAN': request.data.get('PAN'),
            'country': request.data.get('country'),
            'state': request.data.get('state'),
            'city': request.data.get('city'),
            'PIN': request.data.get('PIN'),
            'address': request.data.get('address'),
            'registered_office_address': request.data.get('registered_office_address'),
            'branch_email': request.data.get('branch_email'),
            'branch_phone': request.data.get('branch_phone'),
            'branch_whatsapp': request.data.get('branch_whatsapp')
        }

        # Checking for existing branch name
        if System_branch_details.objects.filter(branch_name=branch_details_data['branch_name']).exists():
            return JsonResponse({'error': 'Branch Name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Serializing and validating the branch details data
        branch_details_serializer = SystemBranchDetailsSerializer(data=branch_details_data)

        if branch_details_serializer.is_valid():
            # Save branch details and get the branch ID
            branch_instance = branch_details_serializer.save()
            branch_id = branch_instance.id

            # Now, use the branch_id to create brand and contact data
            branch_brand_data = {
                'logo': request.FILES.get('logo'),  # Image field
                'favicon': request.FILES.get('favicon'),  # Image field
                'letter_header': request.FILES.get('letter_header'),  # File field
                'letter_footer': request.FILES.get('letter_footer'),  # File field
                'brand_branch_id': branch_id  # Use the generated branch_id
            }

            branch_contact_data = {
                'contact_name': request.data.get('contact_name'),
                'designation': request.data.get('designation'),
                'role': request.data.get('role'),
                'contact_email': request.data.get('contact_email'),
                'contact_no': request.data.get('contact_no'),  # Fixed field name
                'contact_branch_id': branch_id  # Use the generated branch_id
            }

            # Serializing brand and contact data
            branch_brand_serializer = SystemBranchBrandSerializer(data=branch_brand_data)
            branch_contact_serializer = SystemBranchContactSerializer(data=branch_contact_data)

            # Check validity for both serializers
            if branch_brand_serializer.is_valid() and branch_contact_serializer.is_valid():
                # Save brand and contact details
                branch_brand_serializer.save()
                branch_contact_serializer.save()

                return JsonResponse({
                    'branch_details': branch_details_serializer.data,
                    'branch_brand': branch_brand_serializer.data,
                    'branch_contact': branch_contact_serializer.data,
                }, status=status.HTTP_201_CREATED)
            else:
                # If brand or contact serializers fail, rollback
                errors = {
                    'branch_brand_errors': branch_brand_serializer.errors,
                    'branch_contact_errors': branch_contact_serializer.errors
                }
                return JsonResponse(errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse(branch_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            # Fetching all details
            branch_details = System_branch_details.objects.all()
            branch_brand = System_branch_brand.objects.all()
            branch_contact = System_branch_contact.objects.all()

            # Serializing data
            branch_details_serializer = SystemBranchDetailsSerializer(branch_details, many=True)
            branch_brand_serializer = SystemBranchBrandSerializer(branch_brand, many=True)
            branch_contact_serializer = SystemBranchContactSerializer(branch_contact, many=True)

            # Returning JsonResponse
            return JsonResponse({
                'branch_details': branch_details_serializer.data,
                'branch_brand': branch_brand_serializer.data,
                'branch_contact': branch_contact_serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'GET'])
@transaction.atomic
def system_bank_details_handler(request):
    if request.method == 'POST':
        # Parse form-data and handle file uploads
        data_list = []
        i = 0
        while f"bank_name[{i}]" in request.POST:
            data = {
                'bank_name': request.POST.get(f"bank_name[{i}]"),
                'branch_name': request.POST.get(f"branch_name[{i}]"),
                'IFSC': request.POST.get(f"IFSC[{i}]"),
                'account_name': request.POST.get(f"account_name[{i}]"),
                'account_no': request.POST.get(f"account_no[{i}]"),
                'account_type': request.POST.get(f"account_type[{i}]"),
                'bank_logo': request.FILES.get(f"bank_logo[{i}]")  # Handle file upload
            }
            print(data)
            data_list.append(data)
            i += 1

        serializer = SystemBankDetailsSerializer(data=data_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Bank details saved", "data": serializer.data}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400, safe=False)

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
        # Ensure that we can handle both single and multiple instances
        data = request.data
        if not isinstance(data, list):
            data = [data]  # Convert single object to a list if necessary
        print(data)

        serializer = SystemBoardOfDirectorsSerializer(data=data, many=True)  # Handle multiple instances
        if serializer.is_valid():
            serializer.save()  # Save all instances
            return JsonResponse({"message": "Board of Directors details saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
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

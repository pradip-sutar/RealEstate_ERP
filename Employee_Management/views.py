from django.shortcuts import render
from . models import *
from . serializers import *
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import transaction
from rest_framework.response import Response
from collections import defaultdict
import os
from django.conf import settings
# Create your views here.




from .models import *
from .serializers import *

# GET and POST method for handling employee data
@api_view(['POST', 'GET', 'DELETE'])
@transaction.atomic
def employee_data(request):
    if request.method == 'POST':
        # print(request.data)
        # Helper function to split and organize the data by prefix
        def organized_data(data, prefix):
            prefix_data = {}
            for key, value in data.items():
                if key.startswith(prefix):
                    # Extract the field inside the brackets, e.g. company_detail[empid] -> empid
                    field_name = key.split('[')[1][:-1]
                    prefix_data[field_name] = value  # Assuming value is in list form like ['100']
            return prefix_data
        
        def organize_family_data(data, prefix):
            """Organize indexed form data into a list of dictionaries for FamilyProfile JSONField."""
            family_list = []
            index = 0
            
            while True:
                family_member_data = {}
                found = False

                # Iterate through all the key-value pairs in the data
                for key, value in data.items():
                    if key.startswith(f'{prefix}[{index}]'):
                        field_name = key.split('.')[1]  # Extract the field name after the dot (e.g., 'name', 'rel')
                        family_member_data[field_name] = value[0] if isinstance(value, list) and value else value
                        found = True
                
                if not found:
                    break

                family_list.append(family_member_data)
                index += 1

            return family_list

        def organize_education_data(data, prefix, files):
            """
            Organize indexed form data into a list of dictionaries for EducationProfile JSONField.
            Handles file fields separately.
            """
            education_list = []
            index = 0
            
            while True:
                education_data = {}
                found = False
                certificate = None
                marklist = None

                # Iterate through all the key-value pairs in the data
                for key, value in data.items():
                    if key.startswith(f'{prefix}[{index}]'):
                        # Extract the field name after the dot (e.g., 'courceName', 'boardName')
                        field_name = key.split('.')[1]
                        if field_name in ['certificate', 'marklist']:
                            # Handle file fields from the files dictionary
                            if field_name == 'certificate' and f'{prefix}[{index}].certificate' in files:
                                certificate = files[f'{prefix}[{index}].certificate']
                            if field_name == 'marklist' and f'{prefix}[{index}].marklist' in files:
                                marklist = files[f'{prefix}[{index}].marklist']
                        else:
                            # Store other fields in the education_data dictionary
                            education_data[field_name] = value[0] if isinstance(value, list) and value else value
                            found = True

                if not found:
                    break

                # Add the education data to the list
                education_list.append({
                    'details': education_data,
                    'certificate': certificate,
                    'marklist': marklist
                })
                index += 1

            return education_list

        # Extract and organize the data based on the prefix
        company_data = organized_data(request.data, 'company_data')
        # print("company data ..................",company_data)
        address_data= organized_data(request.data, 'address_data')
        # print("adress data ..................",address_data)
        personal_data = organized_data(request.data, 'personal_data')
        # print("personal_data ..................",personal_data)
        family_data = organize_family_data(request.data, 'family_data')
        # print("family_data ..................",family_data)
        education_data_list = organize_education_data(request.data, 'education_data',request.FILES)
        print("education data ..................",education_data_list)
        training_data = organize_family_data(request.data, 'training_data')
        print("training data ..................",training_data)
        Experience_data = organize_education_data(request.data, 'Experience_data',request.FILES)
    
        skills_data = organized_data(request.data, 'skills_data')


        try:
            with transaction.atomic():
                # Save Company Detail
                company_serializer = CompanyProfileSerializer(data=company_data)
                if company_serializer.is_valid():
                    emmployee_instance = company_serializer.save()  # Save and get the instance
                else:
                    return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Attach employee_id to the related details before saving them
                address_data['employee_id'] = emmployee_instance.empid
                personal_data['employee_id'] = emmployee_instance.empid
                
                # Save Address Detail
                Adress_serializer = AddressSerializer(data=address_data)
                if Adress_serializer.is_valid():
                    Adress_serializer.save()
                else:
                    return JsonResponse(Adress_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                #  Save personal Detail
                personal_serializer = PersonalProfileSerializer(data=personal_data)
                if personal_serializer.is_valid():
                    personal_serializer.save()
                else:
                    return JsonResponse(personal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                #  Save family Detail
                employee = Company_profile.objects.get(empid=emmployee_instance.empid)  # Example employee lookup
                family_profile = FamilyProfile(details=family_data, employee_id=employee)
                family_profile.save()

                #  Save education_data Detail
                for education_data in education_data_list:
                    # Extract details and file fields
                    details = education_data['details']
                    certificate = education_data.get('certificate', None)
                    marklist = education_data.get('marklist', None)
                    # Create the EducationProfile instance
                    education_profile = EducationProfile(
                        details=details,
                        certificate=certificate,
                        marklist=marklist,
                        employee_id=employee  # Reference to the employee
                    )
                    education_profile.save()

                #  Save training Detail
                training_profile = Trainig(details=training_data, employee_id=employee)
                training_profile.save()
                
                # #  Save experience Detail
                for data in Experience_data:
                    # Extract details and file fields
                    details = data['details']
                    certificate = data.get('certificate', None)
                    marklist = data.get('marklist', None)
                    # Create the EducationProfile instance
                    education_profile = Experience(
                        details=details,
                        experience_letter=certificate,
                        Joining_letter=marklist,
                        employee_id=employee  # Reference to the employee
                    )
                    education_profile.save()
                
                #  Save skills Detail
                family_profile = Skill_Level(details=skills_data, employee_id=employee)
                family_profile.save()

                return JsonResponse({'message': 'All details saved successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        employee_id = request.query_params.get('employee_id', None)
    
        if employee_id is not None:
            # Fetch the details based on employee_id
            company_data = Company_profile.objects.filter(empid=employee_id)
            Adress_data = Address.objects.filter(employee_id=employee_id)
            personal_data = Personal_Profile.objects.filter(employee_id=employee_id)
            family_data = FamilyProfile.objects.filter(employee_id=employee_id)
            education_data = EducationProfile.objects.filter(employee_id=employee_id)
            training_data = Trainig.objects.filter(employee_id=employee_id)
            Experience_data = Experience.objects.filter(employee_id=employee_id)
            skills_data = Skill_Level.objects.filter(employee_id=employee_id)

            # Serialize the data
            company_serializer = CompanyProfileSerializer(company_data, many=True)
            address_serializer = AddressSerializer(Adress_data, many=True)
            personal_serializer = PersonalProfileSerializer(personal_data, many=True)
            family_serializer = FamilyProfileSerializer(family_data, many=True)
            education_serializer = EducationProfileSerializer(education_data, many=True)  # corrected this line
            training_serializer = TrainigSerializer(training_data, many=True)
            experience_serializer = ExperienceSerializer(Experience_data, many=True)
            skills_serializer = SkillLevelSerializer(skills_data, many=True)

            # Return the serialized data
            return JsonResponse({
                "data": {
                    "company_data": company_serializer.data,
                    "address_data": address_serializer.data,
                    "personal_data": personal_serializer.data,
                    "family_data": family_serializer.data,
                    "education_details": education_serializer.data,
                    "training_details": training_serializer.data,
                    "experience_data": experience_serializer.data,
                    "skills_data": skills_serializer.data
                }
            }, status=200)

        else:
            # Fetch all company details if no employee_id is provided
            company_details = Company_profile.objects.all()
            company_serializer = CompanyProfileSerializer(company_details, many=True)  # corrected here

            return JsonResponse({"data": company_serializer.data}, status=200)

        

@api_view(['GET', 'POST'])
def bank_others_view(request):
    if request.method == 'GET':
        try:
            bank_trainings = Bank_Others.objects.all()
            serializer = BankOthersSerializer(bank_trainings, many=True)
            return JsonResponse({'data': serializer.data},safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = BankOthersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['GET', 'POST'])
def employee_salary_handler(request):
    
    if request.method == 'GET':
        employee_salaries = Employee_Salary.objects.all()
        serializer = EmployeeSalarySerializer(employee_salaries, many=True)
        return JsonResponse({'data':serializer.data}, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = EmployeeSalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#KYC

@api_view(['GET', 'POST'])
def employee_kyc_list(request):
    if request.method == 'GET':
        documents = EmployeeKYC.objects.all()
        serializer = EmployeeKYCDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Retrieve employee ID from request
        employee_id = request.data['employee_id']  # Retrieve the employee ID

        if not employee_id:
            return Response({"error": "Employee ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the employee exists
        try:
            employee = Company_profile.objects.get(empid=employee_id)  # Ensure the Employee model is used here
        except Company_profile.DoesNotExist:
            return Response({"error": "Employee does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Initialize lists for valid documents and errors
        valid_kyc_documents = []
        errors = []

        # Check how many KYC documents are being sent (use a prefix 'document_name' in the request data)
        document_count = len([key for key in request.data if key.startswith('document_name')])

        if document_count == 0:
            return Response({"error": "No KYC documents provided."}, status=status.HTTP_400_BAD_REQUEST)

        for i in range(document_count):
            # Gather data for each KYC document dynamically
            kyc_data = {
                'employee_id': employee.empid,  # The employee ID (same for all KYC docs)
                'document_name': request.data.get(f'document_name[{i}]'),
                'issued_from': request.data.get(f'issued_from[{i}]'),
                'issue_date': request.data.get(f'issue_date[{i}]'),
                'document_number': request.data.get(f'document_number[{i}]'),
                'validity': request.data.get(f'validity[{i}]'),
                'upload': request.FILES.get(f'upload[{i}]')  # Make sure you are passing files properly
            }

            # print(kyc_data)
            # Use the serializer to validate the data
            serializer = EmployeeKYCDocumentSerializer(data=kyc_data)
            if serializer.is_valid():
                serializer.save()
                # valid_kyc_documents.append(serializer.validated_data)
            else:
                # Add validation errors for each invalid KYC document
                errors.append({f"Document {i}": serializer.errors})

        # If no valid documents and there are errors, return the errors
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

        # If there are valid documents, save them in bulk
        if valid_kyc_documents:
            EmployeeKYC.objects.bulk_create(
                [EmployeeKYC(employee=employee, **data) for data in valid_kyc_documents]
            )

        return Response({"message": "All KYC documents created successfully."}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_kyc_detail(request, employee_id):
    try:
        # Fetch the KYC record for the given employee_id
        document = EmployeeKYC.objects.filter(employee_id=employee_id)
    except EmployeeKYC.DoesNotExist:
        return Response({"error": "KYC record not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize and return the KYC record
        serializer = EmployeeKYCDocumentSerializer(document, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the KYC record
        serializer = EmployeeKYCDocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the KYC record
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def get_unique_employee_kyc(request):
    documents = EmployeeKYC.objects.all()
    
    # Use a set to keep track of unique employees (by employee_id)
    unique_employees = set()
    serialized_data = []
    
    for document in documents:
        employee_info = (document.employee_id.empid, document.employee_id.name)
        
        if employee_info not in unique_employees:
            unique_employees.add(employee_info)
            serialized_data.append({
                'employee_id': document.employee_id.empid,
                'employee_name': document.employee_id.name,
                'Status': document.Status
            })

    return Response(serialized_data)



@api_view(['POST'])
def update_status(request):
    # Get employee_id from the request data
    employee_id = request.data.get('employee_id')
    if not employee_id:
        return Response({"error": "Employee ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch all documents with the given employee_id
        documents = EmployeeKYC.objects.filter(employee_id=employee_id)
        if not documents.exists():
            return Response({"error": "No documents found for this employee"}, status=status.HTTP_404_NOT_FOUND)
    except EmployeeKYC.DoesNotExist:
        return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)

    # Extract the new status from the request data
    new_status = request.data.get('Status')
    if not new_status:
        return Response({"error": "Status is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Validate if the new status is in the STATUS_CHOICES
    if new_status not in dict(EmployeeKYC.STATUS_CHOICES):
        return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

    # Update the Status field for all documents associated with the employee_id
    updated_count = 0
    for document in documents:
        document.Status = new_status
        document.save()
        updated_count += 1

    return Response({
        "message": f"Status updated successfully for {updated_count} document(s)", 
        "new_status": new_status
    }, status=status.HTTP_200_OK)



@api_view(['POST'])
def employee_document_rights(request):
    if not isinstance(request.data, list):
        return Response({'error': 'Request data must be a list of objects'}, status=status.HTTP_400_BAD_REQUEST)

    # Iterate over each employee's data in the request
    for item in request.data:
        empid = item.get('empid')

        if not empid:
            return Response({'error': 'empid is required for each employee'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the company profile using the empid
            company_profile = Company_profile.objects.get(empid=empid)
        except Company_profile.DoesNotExist:
            return Response({'error': f'Company profile with empid {empid} not found'}, status=status.HTTP_404_NOT_FOUND)

        # Use serializer to update document_rights or any other fields for each employee
        serializer = CompanyProfileSerializer(company_profile, data=item, partial=True)  # partial=True allows updating specific fields
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

    return Response({'message': 'Data updated successfully for all employees'}, status=status.HTTP_200_OK)




#======================= document master views ======================================#


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def document_master_view(request, pk=None):
    # GET all documents or a single document if pk is provided
    if request.method == 'GET':
        if pk:
            try:
                document = Document_master.objects.get(pk=pk)
                serializer = DocumentMasterSerializer(document)
                return Response(serializer.data)
            except Document_master.DoesNotExist:
                return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            documents = Document_master.objects.all()
            serializer = DocumentMasterSerializer(documents, many=True)
            return Response(serializer.data)
    
    # POST to create one or multiple documents
    elif request.method == 'POST':
        # Check if the data is a list (multiple documents) or a single object
        if isinstance(request.data, list):
            # Handle multiple instances
            serializer = DocumentMasterSerializer(data=request.data, many=True)
        else:
            # Handle single instance
            serializer = DocumentMasterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will create multiple instances if many=True
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PUT (update) an existing document
    elif request.method == 'PUT':
        try:
            document = Document_master.objects.get(pk=pk)
            serializer = DocumentMasterSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Document_master.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # DELETE an existing document
    elif request.method == 'DELETE':
        try:
            document = Document_master.objects.get(pk=pk)
            document.delete()
            return Response({'message': 'Document deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Document_master.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)



#================================== fetch document rights ======================================


@api_view(['GET'])
def doc_rights_fetch(request):
  
    try:
        company_profiles = Company_profile.objects.all()
        serializer = CompanyProfileSerializer(company_profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


#============= Dowmload api =========================#

from django.http import FileResponse, Http404

@api_view(['GET'])
def download_file(request, file_name):
  
    file_path = os.path.join(settings.MEDIA_ROOT, 'employee_documents', file_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        return response
    raise Http404("File does not exist")

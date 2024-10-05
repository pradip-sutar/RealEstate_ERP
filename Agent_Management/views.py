from django.shortcuts import render
from . models import *
from . serializers import *
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import transaction
# Create your views here.


@transaction.atomic
@api_view(['GET', 'POST'])
def agent_type_handler(request):
    if request.method == 'GET':
        # Retrieve all Agent_type instances
        agents = Agent_type.objects.all()
        serializer = AgentTypeSerializer(agents, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK,safe=False)

    elif request.method == 'POST':
        # Create a new Agent_type instance
        serializer = AgentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', 'DELETE'])
@transaction.atomic
def agent_management_handler(request):
    if request.method == 'POST':
        print(request.data)
        # Helper function to split and organize the data by prefix
        def organized_data(data, prefix):
            prefix_data = {}
            for key, value in data.items():
                if key.startswith(prefix):
                    # Extract the field inside the brackets, e.g. company_detail[agentid] -> agentid
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
        # print("education data ..................",education_data_list)
        training_data = organize_family_data(request.data, 'training_data')
        # print("training data ..................",training_data)
        Experience_data = organize_education_data(request.data, 'experience_data',request.FILES)
        print('experience data .....................',Experience_data)
        skills_data = organized_data(request.data, 'skills_data')


        try:
            with transaction.atomic():
                # Save Company Detail
                company_serializer = CompanyProfileSerializer(data=company_data)
                if company_serializer.is_valid():
                    agent_instance = company_serializer.save()  # Save and get the instance
                else:
                    return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Attach agent_id to the related details before saving them
                address_data['agent_id'] = agent_instance.agentid
                personal_data['agent_id'] = agent_instance.agentid
                
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
                agent = Company_profile.objects.get(agentid=agent_instance.agentid)  # Example employee lookup
                family_profile = FamilyProfile(details=family_data, agent_id=agent)
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
                        agent_id=agent  # Reference to the employee
                    )
                    education_profile.save()

                #  Save training Detail
                training_profile = Trainig(details=training_data, agent_id=agent)
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
                        agent_id=agent  # Reference to the employee
                    )
                    education_profile.save()
                
                #  Save skills Detail
                family_profile = Skill_Level(details=skills_data, agent_id=agent)
                family_profile.save()

                return JsonResponse({'message': 'All details saved successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        agent_id = request.query_params.get('agent_id', None)
    
        if agent_id is not None:
            # Fetch the details based on agent_id
            company_data = Company_profile.objects.filter(agentid=agent_id)
            Adress_data = Address.objects.filter(agent_id=agent_id)
            personal_data = Personal_Profile.objects.filter(agent_id=agent_id)
            family_data = FamilyProfile.objects.filter(agent_id=agent_id)
            education_data = EducationProfile.objects.filter(agent_id=agent_id)
            training_data = Trainig.objects.filter(agent_id=agent_id)
            Experience_data = Experience.objects.filter(agent_id=agent_id)
            skills_data = Skill_Level.objects.filter(agent_id=agent_id)

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
            # Fetch all company details if no agent_id is provided
            company_details = Company_profile.objects.all()
            company_serializer = CompanyProfileSerializer(company_details, many=True)  # corrected here

            return JsonResponse({"data": company_serializer.data}, status=200)

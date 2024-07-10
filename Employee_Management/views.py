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
def employee_management_handler(request):
    if request.method == 'POST':
        company_data = request.data.get('company_profile')
        address_data = request.data.get('address')
        personal_profile_data = request.data.get('personal_profile')
        family_profile_data = request.data.get('family_profile')
        education_profile_data = request.data.get('education_profile')
        training_data = request.data.get('training')
        experience_data = request.data.get('experience')
        skill_level_data = request.data.get('skill_level')

        # Company profile
        company_serializer = CompanyProfileSerializer(data=company_data)
        if company_serializer.is_valid():
            company = company_serializer.save()
        else:
            return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Address
        address_data['employee_id'] = company.empid
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
        else:
            return JsonResponse(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Personal profile
        personal_profile_data['employee_id'] = company.empid
        personal_profile_serializer = PersonalProfileSerializer(data=personal_profile_data)
        if personal_profile_serializer.is_valid():
            personal_profile_serializer.save()
        else:
            return JsonResponse(personal_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Family profile
        family_profile_data['employee_id'] = company.empid
        family_profile_serializer = FamilyProfileSerializer(data=family_profile_data)
        if family_profile_serializer.is_valid():
            family_profile_serializer.save()
        else:
            return JsonResponse(family_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Education profile
        education_profile_data['employee_id'] = company.empid
        education_profile_serializer = EducationProfileSerializer(data=education_profile_data)
        if education_profile_serializer.is_valid():
            education_profile_serializer.save()
        else:
            return JsonResponse(education_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Training
        training_data['employee_id'] = company.empid
        training_serializer = TrainigSerializer(data=training_data)
        if training_serializer.is_valid():
            training_serializer.save()
        else:
            return JsonResponse(training_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Experience
        experience_data['employee_id'] = company.empid
        experience_serializer = ExperienceSerializer(data=experience_data)
        if experience_serializer.is_valid():
            experience_serializer.save()
        else:
            return JsonResponse(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Skill level
        skill_level_data['employee_id'] = company.empid
        skill_level_serializer = SkillLevelSerializer(data=skill_level_data)
        if skill_level_serializer.is_valid():
            skill_level_serializer.save()
        else:
            return JsonResponse(skill_level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"message": "Employee data created successfully"}, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        empid = request.query_params.get('empid', None)
        if empid:
            try:
                company = Company_profile.objects.get(empid=empid)
            except Company_profile.DoesNotExist:
                return JsonResponse({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

            company_serializer = CompanyProfileSerializer(company)
            address_serializer = AddressSerializer(Address.objects.get(employee_id=company.empid))
            personal_profile_serializer = PersonalProfileSerializer(Personal_Profile.objects.get(employee_id=company.empid))
            family_profile_serializer = FamilyProfileSerializer(FamilyProfile.objects.get(employee_id=company.empid))
            education_profile_serializer = EducationProfileSerializer(EducationProfile.objects.get(employee_id=company.empid))
            training_serializer = TrainigSerializer(Trainig.objects.get(employee_id=company.empid))
            experience_serializer = ExperienceSerializer(Experience.objects.get(employee_id=company.empid))
            skill_level_serializer = SkillLevelSerializer(Skill_Level.objects.get(employee_id=company.empid))

            data = {
                "company_profile": company_serializer.data,
                "address": address_serializer.data,
                "personal_profile": personal_profile_serializer.data,
                "family_profile": family_profile_serializer.data,
                "education_profile": education_profile_serializer.data,
                "training": training_serializer.data,
                "experience": experience_serializer.data,
                "skill_level": skill_level_serializer.data
            }

            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        else:
            employees = Company_profile.objects.all()
            all_data = []
            for company in employees:
                company_serializer = CompanyProfileSerializer(company)
                address_serializer = AddressSerializer(Address.objects.get(employee_id=company.empid))
                personal_profile_serializer = PersonalProfileSerializer(Personal_Profile.objects.get(employee_id=company.empid))
                family_profile_serializer = FamilyProfileSerializer(FamilyProfile.objects.get(employee_id=company.empid))
                education_profile_serializer = EducationProfileSerializer(EducationProfile.objects.get(employee_id=company.empid))
                training_serializer = TrainigSerializer(Trainig.objects.get(employee_id=company.empid))
                experience_serializer = ExperienceSerializer(Experience.objects.get(employee_id=company.empid))
                skill_level_serializer = SkillLevelSerializer(Skill_Level.objects.get(employee_id=company.empid))

                data = {
                    "company_profile": company_serializer.data,
                    "address": address_serializer.data,
                    "personal_profile": personal_profile_serializer.data,
                    "family_profile": family_profile_serializer.data,
                    "education_profile": education_profile_serializer.data,
                    "training": training_serializer.data,
                    "experience": experience_serializer.data,
                    "skill_level": skill_level_serializer.data
                }

                all_data.append(data)

            return JsonResponse(all_data, status=status.HTTP_200_OK, safe=False)
        

@api_view(['GET', 'POST'])
def bank_others_view(request):
    if request.method == 'GET':
        try:
            bank_others = Bank_Others.objects.all()
            serializer = BankOthersSerializer(bank_others, many=True)
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
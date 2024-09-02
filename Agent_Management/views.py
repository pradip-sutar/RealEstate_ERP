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
def agent_management_handler(request):
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
        address_data['agent_id'] = company.agentid
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
        else:
            return JsonResponse(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Personal profile
        personal_profile_data['agent_id'] = company.agentid
        personal_profile_serializer = PersonalProfileSerializer(data=personal_profile_data)
        if personal_profile_serializer.is_valid():
            personal_profile_serializer.save()
        else:
            return JsonResponse(personal_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Family profile
        family_profile_data['agent_id'] = company.agentid
        family_profile_serializer = FamilyProfileSerializer(data=family_profile_data)
        if family_profile_serializer.is_valid():
            family_profile_serializer.save()
        else:
            return JsonResponse(family_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Education profile
        education_profile_data['agent_id'] = company.agentid
        education_profile_serializer = EducationProfileSerializer(data=education_profile_data)
        if education_profile_serializer.is_valid():
            education_profile_serializer.save()
        else:
            return JsonResponse(education_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Training
        training_data['agent_id'] = company.agentid
        training_serializer = TrainigSerializer(data=training_data)
        if training_serializer.is_valid():
            training_serializer.save()
        else:
            return JsonResponse(training_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Experience
        experience_data['agent_id'] = company.agentid
        experience_serializer = ExperienceSerializer(data=experience_data)
        if experience_serializer.is_valid():
            experience_serializer.save()
        else:
            return JsonResponse(experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Skill level
        skill_level_data['agent_id'] = company.agentid
        skill_level_serializer = SkillLevelSerializer(data=skill_level_data)
        if skill_level_serializer.is_valid():
            skill_level_serializer.save()
        else:
            return JsonResponse(skill_level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"message": "Agent data created successfully"}, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        agentid = request.query_params.get('agentid', None)
        if agentid:
            try:
                company = Company_profile.objects.get(agentid=agentid)
            except Company_profile.DoesNotExist:
                return JsonResponse({"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND)

            company_serializer = CompanyProfileSerializer(company)
            address_serializer = AddressSerializer(Address.objects.get(agent_id=company.agentid))
            personal_profile_serializer = PersonalProfileSerializer(Personal_Profile.objects.get(agent_id=company.agentid))
            family_profile_serializer = FamilyProfileSerializer(FamilyProfile.objects.get(agent_id=company.agentid))
            education_profile_serializer = EducationProfileSerializer(EducationProfile.objects.get(agent_id=company.agentid))
            training_serializer = TrainigSerializer(Trainig.objects.get(agent_id=company.agentid))
            experience_serializer = ExperienceSerializer(Experience.objects.get(agent_id=company.agentid))
            skill_level_serializer = SkillLevelSerializer(Skill_Level.objects.get(agent_id=company.agentid))

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
            agents = Company_profile.objects.all()
            all_data = []
            for company in agents:
                company_serializer = CompanyProfileSerializer(company)
                address_serializer = AddressSerializer(Address.objects.get(agent_id=company.agentid))
                personal_profile_serializer = PersonalProfileSerializer(Personal_Profile.objects.get(agent_id=company.agentid))
                family_profile_serializer = FamilyProfileSerializer(FamilyProfile.objects.get(agent_id=company.agentid))
                education_profile_serializer = EducationProfileSerializer(EducationProfile.objects.get(agent_id=company.agentid))
                training_serializer = TrainigSerializer(Trainig.objects.get(agent_id=company.agentid))
                experience_serializer = ExperienceSerializer(Experience.objects.get(agent_id=company.agentid))
                skill_level_serializer = SkillLevelSerializer(Skill_Level.objects.get(agent_id=company.agentid))

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
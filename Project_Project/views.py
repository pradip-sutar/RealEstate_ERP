from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import transaction
from .models import *
from .serializers import *

# 1. View for Project_subproject_details
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_subproject_details_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id', None)
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        if subproject_id:
            subprojects = Project_subproject_details.objects.filter(id=subproject_id)
        else:
            subprojects = Project_subproject_details.objects.filter(confirm_project_id=confirm_project_id)
        serializer = ProjectSubprojectDetailsSerializer(subprojects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectSubprojectDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Subproject added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        subproject_id = request.query_params.get('subproject_id', None)
        if not subproject_id:
            return JsonResponse({'error': 'Please provide the subproject ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            subproject = Project_subproject_details.objects.get(pk=subproject_id)
        except Project_subproject_details.DoesNotExist:
            return JsonResponse({'error': 'Subproject not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectSubprojectDetailsSerializer(subproject, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Subproject updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subproject_id = request.query_params.get('subproject_id', None)
        if not subproject_id:
            return JsonResponse({'error': 'Please provide the subproject ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            subproject = Project_subproject_details.objects.get(pk=subproject_id)
        except Project_subproject_details.DoesNotExist:
            return JsonResponse({'error': 'Subproject not found'}, status=status.HTTP_404_NOT_FOUND)

        subproject.delete()
        return JsonResponse({"message": "Subproject deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 2. View for Project_Commission
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_commission_handler(request):
    if request.method == 'GET':
        commission_id = request.query_params.get('commission_id', None)
        if commission_id:
            commissions = Project_Commission.objects.filter(id=commission_id)
        else:
            commissions = Project_Commission.objects.all()
        serializer = ProjectCommissionSerializer(commissions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectCommissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Commission added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        commission_id = request.query_params.get('commission_id', None)
        if not commission_id:
            return JsonResponse({'error': 'Please provide the commission ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            commission = Project_Commission.objects.get(pk=commission_id)
        except Project_Commission.DoesNotExist:
            return JsonResponse({'error': 'Commission not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectCommissionSerializer(commission, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Commission updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        commission_id = request.query_params.get('commission_id', None)
        if not commission_id:
            return JsonResponse({'error': 'Please provide the commission ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            commission = Project_Commission.objects.get(pk=commission_id)
        except Project_Commission.DoesNotExist:
            return JsonResponse({'error': 'Commission not found'}, status=status.HTTP_404_NOT_FOUND)

        commission.delete()
        return JsonResponse({"message": "Commission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 3. View for Project_PaymentSlab
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_payment_slab_handler(request):
    if request.method == 'GET':
        slab_id = request.query_params.get('slab_id', None)
        if slab_id:
            slabs = Project_PaymentSlab.objects.filter(id=slab_id)
        else:
            slabs = Project_PaymentSlab.objects.all()
        serializer = ProjectPaymentSlabSerializer(slabs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectPaymentSlabSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Payment slab added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        slab_id = request.query_params.get('slab_id', None)
        if not slab_id:
            return JsonResponse({'error': 'Please provide the payment slab ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            slab = Project_PaymentSlab.objects.get(pk=slab_id)
        except Project_PaymentSlab.DoesNotExist:
            return JsonResponse({'error': 'Payment slab not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectPaymentSlabSerializer(slab, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Payment slab updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        slab_id = request.query_params.get('slab_id', None)
        if not slab_id:
            return JsonResponse({'error': 'Please provide the payment slab ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            slab = Project_PaymentSlab.objects.get(pk=slab_id)
        except Project_PaymentSlab.DoesNotExist:
            return JsonResponse({'error': 'Payment slab not found'}, status=status.HTTP_404_NOT_FOUND)

        slab.delete()
        return JsonResponse({"message": "Payment slab deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_tax_handler(request):
    if request.method == 'GET':
        tax_id = request.query_params.get('tax_id', None)
        if tax_id:
            taxes = Project_Tax.objects.filter(id=tax_id)
        else:
            taxes = Project_Tax.objects.all()
        serializer = ProjectTaxSerializer(taxes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectTaxSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Tax added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        tax_id = request.query_params.get('tax_id', None)
        if not tax_id:
            return JsonResponse({'error': 'Please provide the tax ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tax = Project_Tax.objects.get(pk=tax_id)
        except Project_Tax.DoesNotExist:
            return JsonResponse({'error': 'Tax not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectTaxSerializer(tax, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Tax updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tax_id = request.query_params.get('tax_id', None)
        if not tax_id:
            return JsonResponse({'error': 'Please provide the tax ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tax = Project_Tax.objects.get(pk=tax_id)
        except Project_Tax.DoesNotExist:
            return JsonResponse({'error': 'Tax not found'}, status=status.HTTP_404_NOT_FOUND)

        tax.delete()
        return JsonResponse({"message": "Tax deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 2. View for Project_Amenity
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_amenity_handler(request):
    if request.method == 'GET':
        amenity_id = request.query_params.get('amenity_id', None)
        if amenity_id:
            amenities = Project_Amenity.objects.filter(id=amenity_id)
        else:
            amenities = Project_Amenity.objects.all()
        serializer = ProjectAmenitySerializer(amenities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Amenity added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        amenity_id = request.query_params.get('amenity_id', None)
        if not amenity_id:
            return JsonResponse({'error': 'Please provide the amenity ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amenity = Project_Amenity.objects.get(pk=amenity_id)
        except Project_Amenity.DoesNotExist:
            return JsonResponse({'error': 'Amenity not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectAmenitySerializer(amenity, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Amenity updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        amenity_id = request.query_params.get('amenity_id', None)
        if not amenity_id:
            return JsonResponse({'error': 'Please provide the amenity ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amenity = Project_Amenity.objects.get(pk=amenity_id)
        except Project_Amenity.DoesNotExist:
            return JsonResponse({'error': 'Amenity not found'}, status=status.HTTP_404_NOT_FOUND)

        amenity.delete()
        return JsonResponse({"message": "Amenity deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 3. View for Project_PaidAmenity
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_paid_amenity_handler(request):
    if request.method == 'GET':
        paid_amenity_id = request.query_params.get('paid_amenity_id', None)
        if paid_amenity_id:
            paid_amenities = Project_PaidAmenity.objects.filter(id=paid_amenity_id)
        else:
            paid_amenities = Project_PaidAmenity.objects.all()
        serializer = ProjectPaidAmenitySerializer(paid_amenities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectPaidAmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Paid Amenity added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        paid_amenity_id = request.query_params.get('paid_amenity_id', None)
        if not paid_amenity_id:
            return JsonResponse({'error': 'Please provide the paid amenity ID for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            paid_amenity = Project_PaidAmenity.objects.get(pk=paid_amenity_id)
        except Project_PaidAmenity.DoesNotExist:
            return JsonResponse({'error': 'Paid Amenity not found'}, status=status.HTTP_404_NOT_FOUND)

        partial = request.method == 'PATCH'
        serializer = ProjectPaidAmenitySerializer(paid_amenity, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Paid Amenity updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        paid_amenity_id = request.query_params.get('paid_amenity_id', None)
        if not paid_amenity_id:
            return JsonResponse({'error': 'Please provide the paid amenity ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            paid_amenity = Project_PaidAmenity.objects.get(pk=paid_amenity_id)
        except Project_PaidAmenity.DoesNotExist:
            return JsonResponse({'error': 'Paid Amenity not found'}, status=status.HTTP_404_NOT_FOUND)

        paid_amenity.delete()
        return JsonResponse({"message": "Paid Amenity deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def nearby_handler(request):
    if request.method == 'GET':
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        if confirm_project_id:
            nearby = NearBy.objects.filter(confirm_project_id=confirm_project_id)
        else:
            nearby = NearBy.objects.all()
        serializer = NearBySerializer(nearby, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = NearBySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        confirm_project_id = request.query_params.get('confirm_project_id')
        nearby = NearBy.objects.get(confirm_project_id=confirm_project_id)
        serializer = NearBySerializer(nearby, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        confirm_project_id = request.query_params.get('confirm_project_id')
        nearby = NearBy.objects.get(confirm_project_id=confirm_project_id)
        nearby.delete()
        return JsonResponse({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ProjectSpecification View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_specification_handler(request):
    if request.method == 'GET':
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        if confirm_project_id:
            specifications = ProjectSpecification.objects.filter(confirm_project_id=confirm_project_id)
        else:
            specifications = ProjectSpecification.objects.all()
        serializer = ProjectSpecificationSerializer(specifications, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        confirm_project_id = request.query_params.get('confirm_project_id')
        specification = ProjectSpecification.objects.get(confirm_project_id=confirm_project_id)
        serializer = ProjectSpecificationSerializer(specification, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        confirm_project_id = request.query_params.get('confirm_project_id')
        specification = ProjectSpecification.objects.get(confirm_project_id=confirm_project_id)
        specification.delete()
        return JsonResponse({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ProjectImages View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def project_images_handler(request):
    if request.method == 'GET':
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        if confirm_project_id:
            images = ProjectImages.objects.filter(confirm_project_id=confirm_project_id)
        else:
            images = ProjectImages.objects.all()
        serializer = ProjectImagesSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        confirm_project_id = request.query_params.get('confirm_project_id')
        image_instance = ProjectImages.objects.get(confirm_project_id=confirm_project_id)
        serializer = ProjectImagesSerializer(image_instance, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        confirm_project_id = request.query_params.get('confirm_project_id')
        image_instance = ProjectImages.objects.get(confirm_project_id=confirm_project_id)
        image_instance.delete()
        return JsonResponse({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
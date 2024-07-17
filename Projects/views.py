from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Project_Type
from .serializers import *
from rest_framework.decorators import api_view
from django.db import transaction

@api_view(['GET', 'POST'])
def project_type_handler(request):
    if request.method == 'GET':
        project_types = Project_Type.objects.all()
        serializer = ProjectTypeSerializer(project_types, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print(request.data)
        serializer = ProjectTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def project_payment_schedules_handler(request):
    if request.method == 'GET':
        schedules = Project_Payment_Schedule.objects.all()
        serializer = ProjectPaymentScheduleSerializer(schedules, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectPaymentScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def project_product_types_handler(request):
    if request.method == 'GET':
        product_types = Project_Product_Type.objects.all()
        serializer = ProjectProductTypeSerializer(product_types, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectProductTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def project_raisecost_types_handler(request):
    if request.method == 'GET':
        raisecost_types = Project_RaiseCost_Type.objects.all()
        serializer = ProjectRaiseCostTypeSerializer(raisecost_types, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectRaiseCostTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def project_amenity_master_list(request):
    if request.method == 'GET':
        amenity_masters = Project_Amenity_Master.objects.all()
        serializer = ProjectAmenityMasterSerializer(amenity_masters, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectAmenityMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def project_nearby_segment_list(request):
    if request.method == 'GET':
        nearby_segments = Project_Nearby_Segment.objects.all()
        serializer = ProjectNearbySegmentSerializer(nearby_segments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectNearbySegmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def project_facing_master_list(request):
    if request.method == 'GET':
        facing_masters = Project_Facing_Master.objects.all()
        serializer = ProjectFacingMasterSerializer(facing_masters, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectFacingMasterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def project_commission_list(request):
    if request.method == 'GET':
        commissions = Project_Commission.objects.all()
        serializer = ProjectCommissionSerializer(commissions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectCommissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def product_ownership_list(request):
    if request.method == 'GET':
        ownerships = Product_Ownership.objects.all()
        serializer = ProductOwnershipSerializer(ownerships, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductOwnershipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def product_approval_body_list(request):
    if request.method == 'GET':
        approval_bodies = Product_ApprovalBody.objects.all()
        serializer = ProductApprovalBodySerializer(approval_bodies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductApprovalBodySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def project_tax_list(request):
    if request.method == 'GET':
        taxes = Project_Tax.objects.all()
        serializer = ProjectTaxSerializer(taxes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectTaxSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def project_product_list(request):
    if request.method == 'GET':
        products = Project_Product.objects.all()
        serializer = ProjectProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    

@api_view(['GET', 'POST'])
def project_add_payment_list_handler(request):
    if request.method == 'GET':
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        print(confirm_project_id)
        if confirm_project_id:
            payments = Project_add_Payment.objects.filter(confirm_project_id=confirm_project_id)
        else:
            payments = Project_add_Payment.objects.all()
        
        serializer = ProjectAddPaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectAddPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
@api_view(['GET', 'POST'])
def project_add_amenity_list_handler(request):
    if request.method == 'GET':
        amenities = Project_add_Amenity.objects.all()
        serializer = ProjectAddAmenitySerializer(amenities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProjectAddAmenitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    

@api_view(['GET', 'POST'])
@transaction.atomic
def project_add_commission_handler(request):
    if request.method == 'GET':
        confirm_project_id = request.query_params.get('confirm_project_id', None)
        if confirm_project_id:
            commission = Project_add_Commission.objects.filter(confirm_project_id=confirm_project_id)
        else:
            commission = Project_add_Commission.objects.all()
        
        serializer = ProjectAddCommissionSerializer(commission, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAddCommissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Commission added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST'])
@transaction.atomic
def project_add_tax_handler(request):
    if request.method == 'GET':
        taxes = Project_add_Tax.objects.all()
        serializer = ProjectAddTaxSerializer(taxes, many=True)
        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAddTaxSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Tax added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@transaction.atomic
def project_add_paid_amenity_handler(request):
    if request.method == 'GET':
        paid_amenities = Project_add_PaidAmenity.objects.all()
        serializer = ProjectAddPaidAmenitySerializer(paid_amenities, many=True)
        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAddPaidAmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Paid amenity added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@transaction.atomic
def project_add_price_handler(request):
    if request.method == 'GET':
        prices = Project_add_Price.objects.all()
        serializer = ProjectAddPriceSerializer(prices, many=True)
        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAddPriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Price added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@transaction.atomic
def project_add_inventory_handler(request):
    if request.method == 'GET':
        inventories = Project_add_Inventory.objects.all()
        serializer = ProjectAddInventorySerializer(inventories, many=True)
        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = ProjectAddInventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Inventory added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
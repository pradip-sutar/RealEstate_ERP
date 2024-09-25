from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# ProductSpecification View
@api_view(['GET', 'POST'])
def product_specification_view(request):
    if request.method == 'GET':
        specifications = ProductSpecification.objects.all()
        serializer = ProductSpecificationSerializer(specifications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ProductImage View
@api_view(['GET', 'POST'])
def product_image_view(request):
    if request.method == 'GET':
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# EnquirySummary View
@api_view(['GET', 'POST'])
def enquiry_summary_view(request):
    if request.method == 'GET':
        enquiries = EnquirySummary.objects.all()
        serializer = EnquirySummarySerializer(enquiries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EnquirySummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# VisitSummary View
@api_view(['GET', 'POST'])
def visit_summary_view(request):
    if request.method == 'GET':
        visits = VisitSummary.objects.all()
        serializer = VisitSummarySerializer(visits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VisitSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# QuoteSummary View
@api_view(['GET', 'POST'])
def quote_summary_view(request):
    if request.method == 'GET':
        quotes = QuoteSummary.objects.all()
        serializer = QuoteSummarySerializer(quotes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuoteSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# EmployeeStatus View
@api_view(['GET', 'POST'])
def employee_status_view(request):
    if request.method == 'GET':
        statuses = EmployeeStatus.objects.all()
        serializer = EmployeeStatusSerializer(statuses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CustomerInformation View
@api_view(['GET', 'POST'])
def customer_information_view(request):
    if request.method == 'GET':
        customers = CustomerInformation.objects.all()
        serializer = CustomerInformationSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CommissionDetails View
@api_view(['GET', 'POST'])
def commission_details_view(request):
    if request.method == 'GET':
        commissions = CommissionDetails.objects.all()
        serializer = CommissionDetailsSerializer(commissions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommissionDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PaymentDetails View
@api_view(['GET', 'POST'])
def payment_details_view(request):
    if request.method == 'GET':
        payments = PaymentDetails.objects.all()
        serializer = PaymentDetailsSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CustomerDocument View
@api_view(['GET', 'POST'])
def customer_document_view(request):
    if request.method == 'GET':
        documents = CustomerDocument.objects.all()
        serializer = CustomerDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PropertyDocument View
@api_view(['GET', 'POST'])
def property_document_view(request):
    if request.method == 'GET':
        properties = PropertyDocument.objects.all()
        serializer = PropertyDocumentSerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertyDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

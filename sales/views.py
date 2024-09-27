from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentReceipt, PaymentSchedule, SalesAgreement
from .serializers import PaymentReceiptSerializer, PaymentScheduleSerializer, SalesAgreementSerializer


# View for PaymentReceipt - Get list and retrieve by ID
@api_view(['GET', 'POST'])
def payment_receipt_list(request):
    if request.method == 'GET':
        receipts = PaymentReceipt.objects.all()
        serializer = PaymentReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def payment_receipt_detail(request, sales_id):
    try:
        receipt = PaymentReceipt.objects.get(sales_id=sales_id)
    except PaymentReceipt.DoesNotExist:
        return Response({"error": "PaymentReceipt not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PaymentReceiptSerializer(receipt)
    return Response(serializer.data)


# View for PaymentSchedule - Get list and retrieve by ID
@api_view(['GET', 'POST'])
def payment_schedule_list(request):
    if request.method == 'GET':
        schedules = PaymentSchedule.objects.all()
        serializer = PaymentScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def payment_schedule_detail(request, sales_id):
    try:
        schedule = PaymentSchedule.objects.get(sales_id=sales_id)
    except PaymentSchedule.DoesNotExist:
        return Response({"error": "PaymentSchedule not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PaymentScheduleSerializer(schedule)
    return Response(serializer.data)


# View for SalesAgreement - Get list and retrieve by ID
@api_view(['GET', 'POST'])
def sales_agreement_list(request):
    if request.method == 'GET':
        agreements = SalesAgreement.objects.all()
        serializer = SalesAgreementSerializer(agreements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SalesAgreementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sales_agreement_detail(request, sales_id):
    try:
        agreement = SalesAgreement.objects.get(sales_id=sales_id)
    except SalesAgreement.DoesNotExist:
        return Response({"error": "SalesAgreement not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SalesAgreementSerializer(agreement)
    return Response(serializer.data)

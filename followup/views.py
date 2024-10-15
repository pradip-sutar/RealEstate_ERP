from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def enquiry_view(request, enquiry_id=None):
    # Handling GET request
    if request.method == 'GET':
        if enquiry_id:
            try:
                enquiry = Enquiry.objects.get(pk=enquiry_id)
                serializer = EnquirySerializer(enquiry)
                return Response(serializer.data)
            except Enquiry.DoesNotExist:
                return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            enquiries = Enquiry.objects.all()
            serializer = EnquirySerializer(enquiries, many=True)
            return Response(serializer.data)

    # Handling POST request
    if request.method == 'POST':
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling PUT request
    if request.method == 'PUT':
        try:
            enquiry = Enquiry.objects.get(pk=enquiry_id)
        except Enquiry.DoesNotExist:
            return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EnquirySerializer(enquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling DELETE request
    if request.method == 'DELETE':
        try:
            enquiry = Enquiry.objects.get(pk=enquiry_id)
            enquiry.delete()
            return Response({'message': 'Enquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Enquiry.DoesNotExist:
            return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)






@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def quotation_view(request, quote_id=None):
    # Handling GET request
    if request.method == 'GET':
        if quote_id:
            try:
                quotation = Quotation.objects.get(pk=quote_id)
                serializer = QuotationSerializer(quotation)
                return Response(serializer.data)
            except Quotation.DoesNotExist:
                return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            quotations = Quotation.objects.all()
            serializer = QuotationSerializer(quotations, many=True)
            return Response(serializer.data)

    # Handling POST request
    if request.method == 'POST':
        serializer = QuotationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling PUT request
    if request.method == 'PUT':
        try:
            quotation = Quotation.objects.get(pk=quote_id)
        except Quotation.DoesNotExist:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuotationSerializer(quotation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling DELETE request
    if request.method == 'DELETE':
        try:
            quotation = Quotation.objects.get(pk=quote_id)
            quotation.delete()
            return Response({'message': 'Quotation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Quotation.DoesNotExist:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)





@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def visit_view(request, quote_id=None):
    # Handling GET request
    if request.method == 'GET':
        if quote_id:
            try:
                visit = Visit.objects.get(pk=quote_id)
                serializer = VisitSerializer(visit)
                return Response(serializer.data)
            except Visit.DoesNotExist:
                return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            visits = Visit.objects.all()
            serializer = VisitSerializer(visits, many=True)
            return Response(serializer.data)

    # Handling POST request
    if request.method == 'POST':
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling PUT request
    if request.method == 'PUT':
        try:
            visit = Visit.objects.get(pk=quote_id)
        except Visit.DoesNotExist:
            return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VisitSerializer(visit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling DELETE request
    if request.method == 'DELETE':
        try:
            visit = Visit.objects.get(pk=quote_id)
            visit.delete()
            return Response({'message': 'Visit deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Visit.DoesNotExist:
            return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)

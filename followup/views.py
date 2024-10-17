from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def enquiry_view(request):
    """
    Handles CRUD operations for Enquiry.
    """
    enquiry_id = request.query_params.get('enquiry_id')

    # GET method
    if request.method == 'GET':
        if enquiry_id:
            enquiry = Enquiry.objects.filter(pk=enquiry_id).first()
            if enquiry:
                serializer = EnquirySerializer(enquiry)
                return Response(serializer.data)
            return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            enquiries = Enquiry.objects.all()
            serializer = EnquirySerializer(enquiries, many=True)
            return Response(serializer.data)

    # POST method
    elif request.method == 'POST':
        print(request.data)
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method
    elif request.method == 'PUT':
        if not enquiry_id:
            return Response({'error': 'Enquiry ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        
        enquiry = Enquiry.objects.filter(pk=enquiry_id).first()
        if not enquiry:
            return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EnquirySerializer(enquiry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method
    elif request.method == 'DELETE':
        if not enquiry_id:
            return Response({'error': 'Enquiry ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        enquiry = Enquiry.objects.filter(pk=enquiry_id).first()
        if not enquiry:
            return Response({'error': 'Enquiry not found'}, status=status.HTTP_404_NOT_FOUND)
        
        enquiry.delete()
        return Response({'message': 'Enquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def quotation_view(request):
    """
    Handles CRUD operations for Quotation.
    """
    quote_id = request.query_params.get('quote_id')

    # GET method
    if request.method == 'GET':
        if quote_id:
            quotation = Quotation.objects.filter(pk=quote_id).first()
            if quotation:
                serializer = QuotationSerializer(quotation)
                return Response(serializer.data)
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            quotations = Quotation.objects.all()
            serializer = QuotationSerializer(quotations, many=True)
            return Response(serializer.data)

    # POST method
    elif request.method == 'POST':
        serializer = QuotationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method
    elif request.method == 'PUT':
        if not quote_id:
            return Response({'error': 'Quotation ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        
        quotation = Quotation.objects.filter(pk=quote_id).first()
        if not quotation:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuotationSerializer(quotation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method
    elif request.method == 'DELETE':
        if not quote_id:
            return Response({'error': 'Quotation ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        quotation = Quotation.objects.filter(pk=quote_id).first()
        if not quotation:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        quotation.delete()
        return Response({'message': 'Quotation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def visit_view(request):
    """
    Handles CRUD operations for Visit.
    """
    visit_id = request.query_params.get('id')

    # Handling GET request
    if request.method == 'GET':
        if id:
            visit = Visit.objects.filter(pk=id).first()
            if visit:
                serializer = VisitSerializer(visit)
                return Response(serializer.data)
            return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            visits = Visit.objects.all()
            serializer = VisitSerializer(visits, many=True)
            return Response(serializer.data)

    # Handling POST request
    elif request.method == 'POST':
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling PUT request
    elif request.method == 'PUT':
        if not id:
            return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        
        visit = Visit.objects.filter(pk=id).first()
        if not visit:
            return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VisitSerializer(visit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handling DELETE request
    elif request.method == 'DELETE':
        if not id:
            return Response({'error': 'Visit ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        visit = Visit.objects.filter(pk=id).first()
        if not visit:
            return Response({'error': 'Visit not found'}, status=status.HTTP_404_NOT_FOUND)
        
        visit.delete()
        return Response({'message': 'Visit deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def site_visit_schedule_view(request):
    visit_id = request.query_params.get('visit_id')

    if request.method == 'GET':
        if visit_id:
            visit = get_object_or_404(Site_visit_schedule, visit_id=visit_id)
            serializer = SiteVisitScheduleSerializer(visit)
            return Response(serializer.data)
        else:
            visits = Site_visit_schedule.objects.all()
            serializer = SiteVisitScheduleSerializer(visits, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SiteVisitScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if not visit_id:
            return Response({"error": "visit_id is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        visit = get_object_or_404(Site_visit_schedule, visit_id=visit_id)
        serializer = SiteVisitScheduleSerializer(visit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not visit_id:
            return Response({"error": "visit_id is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        
        visit = get_object_or_404(Site_visit_schedule, visit_id=visit_id)
        visit.delete()
        return Response({'message': 'Visit deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

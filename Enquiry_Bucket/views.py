from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET', 'POST', 'PUT'])
def quotation_type_handler(request):
    if request.method == 'GET':
        # If `id` is provided in the query params, retrieve the specific object
        quotation_id = request.query_params.get('id', None)
        if quotation_id:
            try:
                quotation_type = Quotation_Type.objects.get(id=quotation_id)
            except Quotation_Type.DoesNotExist:
                return Response({'message': 'The quotation type does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = QuotationTypeSerializer(quotation_type)
            return Response(serializer.data)
        # Otherwise, retrieve all objects
        else:
            quotation_types = Quotation_Type.objects.all()
            serializer = QuotationTypeSerializer(quotation_types, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuotationTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        quotation_id = request.query_params.get('id', None)
        if not quotation_id:
            return Response({'message': 'Quotation type ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            quotation_type = Quotation_Type.objects.get(id=quotation_id)
        except Quotation_Type.DoesNotExist:
            return Response({'message': 'The quotation type does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuotationTypeSerializer(quotation_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST', 'PUT'])
def visit_type_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Visit_Type.objects.get(id=obj_id)
            except Visit_Type.DoesNotExist:
                return Response({'message': 'The visit type does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = VisitTypeSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Visit_Type.objects.all()
            serializer = VisitTypeSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VisitTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Visit type ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Visit_Type.objects.get(id=obj_id)
        except Visit_Type.DoesNotExist:
            return Response({'message': 'The visit type does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VisitTypeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def communication_type_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Communication_Type.objects.get(id=obj_id)
            except Communication_Type.DoesNotExist:
                return Response({'message': 'The communication type does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CommunicationTypeSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Communication_Type.objects.all()
            serializer = CommunicationTypeSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunicationTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Communication type ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Communication_Type.objects.get(id=obj_id)
        except Communication_Type.DoesNotExist:
            return Response({'message': 'The communication type does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommunicationTypeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def source_type_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Source_Type.objects.get(id=obj_id)
            except Source_Type.DoesNotExist:
                return Response({'message': 'The source type does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = SourceTypeSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Source_Type.objects.all()
            serializer = SourceTypeSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SourceTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Source type ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Source_Type.objects.get(id=obj_id)
        except Source_Type.DoesNotExist:
            return Response({'message': 'The source type does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SourceTypeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def enquiry_type_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Enquiry_Type.objects.get(id=obj_id)
            except Enquiry_Type.DoesNotExist:
                return Response({'message': 'The enquiry type does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = EnquiryTypeSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Enquiry_Type.objects.all()
            serializer = EnquiryTypeSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EnquiryTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Enquiry type ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Enquiry_Type.objects.get(id=obj_id)
        except Enquiry_Type.DoesNotExist:
            return Response({'message': 'The enquiry type does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EnquiryTypeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def lead_enquiry_stage_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Lead_Enquiry_Stage.objects.get(id=obj_id)
            except Lead_Enquiry_Stage.DoesNotExist:
                return Response({'message': 'The lead enquiry stage does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = LeadEnquiryStageSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Lead_Enquiry_Stage.objects.all()
            serializer = LeadEnquiryStageSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeadEnquiryStageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Lead enquiry stage ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Lead_Enquiry_Stage.objects.get(id=obj_id)
        except Lead_Enquiry_Stage.DoesNotExist:
            return Response({'message': 'The lead enquiry stage does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeadEnquiryStageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def lead_enquiry_status_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Lead_Enquiry_Status.objects.get(id=obj_id)
            except Lead_Enquiry_Status.DoesNotExist:
                return Response({'message': 'The lead enquiry status does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = LeadEnquiryStatusSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Lead_Enquiry_Status.objects.all()
            serializer = LeadEnquiryStatusSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeadEnquiryStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Lead enquiry status ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Lead_Enquiry_Status.objects.get(id=obj_id)
        except Lead_Enquiry_Status.DoesNotExist:
            return Response({'message': 'The lead enquiry status does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeadEnquiryStatusSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def customer_form_handler(request):
    if request.method == 'GET':
        obj_id = request.query_params.get('id', None)
        if obj_id:
            try:
                obj = Customer_Form.objects.get(id=obj_id)
            except Customer_Form.DoesNotExist:
                return Response({'message': 'The customer form does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerFormSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Customer_Form.objects.all()
            serializer = CustomerFormSerializer(objs, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj_id = request.query_params.get('id', None)
        if not obj_id:
            return Response({'message': 'Customer form ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Customer_Form.objects.get(id=obj_id)
        except Customer_Form.DoesNotExist:
            return Response({'message': 'The customer form does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomerFormSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def customer_form_list(request):
    if request.method == 'GET':
        forms = Customer_Form.objects.all()
        serializer = CustomerFormSerializer(forms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_form_detail(request, pk):
    try:
        form = Customer_Form.objects.get(pk=pk)
    except Customer_Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerFormSerializer(form)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerFormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

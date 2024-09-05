from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET', 'POST', 'PUT'])
def roles_handler(request):
    roles_id = request.query_params.get('id')

    if request.method == 'GET':
        if roles_id:
            try:
                module = Roles.objects.get(pk=roles_id)
                serializer = RolesSerializer(Roles)
            except Roles.DoesNotExist:
                return Response({'error': 'Roles not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            modules = Roles.objects.all()
            serializer = RolesSerializer(modules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if roles_id:
            try:
                module = Roles.objects.get(pk=roles_id)
            except Roles.DoesNotExist:
                return Response({'error': 'Roles not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = RolesSerializer(module, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def rights_handler(request):
    rights_id = request.query_params.get('id')

    if request.method == 'GET':
        if rights_id:
            try:
                module = Rights.objects.get(pk=rights_id)
                serializer = RightsSerializer(Rights)
            except Rights.DoesNotExist:
                return Response({'error': 'Rights not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            modules = Rights.objects.all()
            serializer = RightsSerializer(modules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = RightsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if rights_id:
            try:
                module = Rights.objects.get(pk=rights_id)
            except Rights.DoesNotExist:
                return Response({'error': 'Rights not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = RightsSerializer(module, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
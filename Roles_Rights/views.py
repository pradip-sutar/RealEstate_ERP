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
            roles = Roles.objects.all()
            latest_modules = []
            for role in roles:
                try:
                    latest_right = Rights.objects.filter(roles_id=role).latest('id')
                    latest_modules.append(latest_right)
                except Rights.DoesNotExist:
                    continue
            serializer = RightsSerializer(latest_modules, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        rights = request.data['rights']
        response_data = []  
        errors = []

        for right in rights:
            data = {
                'roles': int(right['role']),
                'view': right['permissions']['view'],
                'write': right['permissions']['write'],
                'edit': right['permissions']['edit'],
                'delete': right['permissions']['delete']
            }

            serializer = RightsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response_data.append(serializer.data)  # Append each serialized data
            else:
                errors.append(serializer.errors)  # Collect errors
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data, status=status.HTTP_201_CREATED)

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
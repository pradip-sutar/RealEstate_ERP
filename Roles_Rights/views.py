from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Roles
from .serializers import RolesSerializer

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


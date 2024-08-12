from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Module
from .serializers import ModuleSerializer

@api_view(['GET', 'POST', 'PUT'])
def module_handler(request):
    module_id = request.query_params.get('id')

    if request.method == 'GET':
        if module_id:
            try:
                module = Module.objects.get(pk=module_id)
                serializer = ModuleSerializer(module)
            except Module.DoesNotExist:
                return Response({'error': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            modules = Module.objects.all()
            serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if module_id:
            try:
                module = Module.objects.get(pk=module_id)
            except Module.DoesNotExist:
                return Response({'error': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ModuleSerializer(module, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)


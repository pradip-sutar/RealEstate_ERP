# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team_Management
from .serializers import TeamManagementSerializer

@api_view(['GET', 'POST'])
def team_management_handler(request):
    if request.method == 'GET':
        teams = Team_Management.objects.all()
        serializer = TeamManagementSerializer(teams, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TeamManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

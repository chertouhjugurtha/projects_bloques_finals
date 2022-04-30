
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projets
from .serialisers import projectsSetSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions

class ProjetsViewSet(APIView):
    # permission_classes = (permissions.AllowAny,)

    # Refer to https://stackoverflow.com/a/35987077/1677041
    permission_classes_by_action = {
        'create': (permissions.IsAdminUser,),
        'list': (permissions.IsAuthenticatedOrReadOnly,),
        'retrieve': (permissions.AllowAny,),
        'update': (permissions.AllowAny,),
        'destroy': (permissions.IsAdminUser,),
        # 'search': (permissions.IsAuthenticated,) 
    }
    def post(self, request):
        serializer = projectsSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        data = request.data
        if "Projets" in data:
            try:
                projets = Projets.objects.get(id=pk)
                
            except projets.DoesNotExist:
                return Response({"erreur": "projets introuvable"}, status=status.HTTP_404_NOT_FOUND)
            project = {"project": data["project"]}
            project_serializer = projectsSetSerializer(project, data=project, partial=True)
            if project_serializer.is_valid():
                project_serializer.save()
                return Response(project_serializer.data, status=status.HTTP_200_OK)
            else:
                Response(project.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     snippet = Projets.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
# import json
# @api_view([ 'GET'])
# def get_projects(request):
#     params=request.params
#     projet=Projets.objects.all()
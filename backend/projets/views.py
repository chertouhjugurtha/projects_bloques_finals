
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projets
from .serialisers import projectsSetSerializer
from rest_framework import status


class ProjetsViewSet(APIView):

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
    
    def delete(self, request, pk, format=None):
        snippet = Projets.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
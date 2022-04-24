from functools import cache
from rest_framework.response import Response
from .models import Activite
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import ActiviteSetSerializer
from rest_framework.decorators import api_view

class ActiviteViewSet(APIView):
    def post(self, request):
        serializer = ActiviteSetSerializer(data=request.data,many=True)
            # serializer = ActiviteSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        data=request.data  
        try:
            activite = Activite.objects.get(id=pk)
        except Activite.DoesNotExist:
            return Response({"erreur": "activite introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['activite']=data["activite"]
        activite_serializer = ActiviteSetSerializer(activite, data=data, partial=True)
        if activite_serializer.is_valid():
            activite_serializer.save()
            return Response(activite_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(activite.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Activite.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

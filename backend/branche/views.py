from functools import cache
from rest_framework.response import Response
from .models import Branche
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import BrancheSetSerializer
from rest_framework.decorators import api_view

class BrancheViewSet(APIView):

    def post(self, request):
        
        serializer = BrancheSetSerializer(data=request.data,many=True)
            # serializer = BrancheSetSerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        data=request.data  
        
        try:
            branche = Branche.objects.get(id=pk)
        except Branche.DoesNotExist:
            return Response({"erreur": "branche introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['branche']=data["branche"]
        
        branche_serializer = BrancheSetSerializer(branche, data=data, partial=True)
        if branche_serializer.is_valid():
            
            branche_serializer.save()
            return Response(branche_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(branche.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Branche.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.response import Response
from .models import Debloqueur
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import DebloqueurSetSerializer

class DebloqueurViewSet(APIView):

    def post(self, request):
        
        serializer = DebloqueurSetSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data=request.data  
        
        try:
            debloqueur = Debloqueur.objects.get(id=pk)
        except Debloqueur.DoesNotExist:
            return Response({"erreur": "debloqueur introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['debloqueur']=data["debloqueur"]
        
        debloqueur_serializer = DebloqueurSetSerializer(debloqueur, data=data, partial=True)
        if debloqueur_serializer.is_valid():
            
            debloqueur_serializer.save()
            return Response(debloqueur_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(debloqueur.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Debloqueur.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
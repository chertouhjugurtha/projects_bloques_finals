from rest_framework.response import Response
from .models import Ministere
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import MinistereSetSerializer







class MinistereViewSet(APIView):

    def post(self, request):
        
        serializer = MinistereSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
       
        
        try:
            ministere = Ministere.get_object(pk)
        except Ministere.DoesNotExist:
            return Response({"erreur": "ministere introuvable"}, status=status.HTTP_404_NOT_FOUND)
        
        ministere = {"ministere": data["ministere"],
        "address": data["address"],
        "phone":data["phone"]}
        ministere_serializer = MinistereSetSerializer(ministere, data=ministere, partial=True)
        if ministere_serializer.is_valid():
            ministere_serializer.save()
            return Response(ministere_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(ministere.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Ministere.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
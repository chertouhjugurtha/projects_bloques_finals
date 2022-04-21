from rest_framework.response import Response
from .models import Wilaya
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import WilayaSetSerializer

class WilayaViewSet(APIView):

    def post(self, request):
        
        serializer = WilayaSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        if "wilaya" in data:
            try:
                wilaya = Wilaya.get_object(pk)
            except Wilaya.DoesNotExist:
                return Response({"erreur": "wilaya introuvable"}, status=status.HTTP_404_NOT_FOUND)
            wilaya = {"wilaya": data["wilaya"]}
            wilaya_serializer = WilayaSetSerializer(wilaya, data=wilaya, partial=True)
            if wilaya_serializer.is_valid():
                wilaya_serializer.save()
                return Response(wilaya_serializer.data, status=status.HTTP_200_OK)
            else:
                Response(wilaya.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Wilaya.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
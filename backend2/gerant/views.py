
from rest_framework.response import Response
from .models import Gerant
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import GerantSetSerializer

class GerantViewSet(APIView):

    def post(self, request):
        
        serializer = GerantSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        if "gerant" in data:
            try:
                gerant = Gerant.objects.get(id=pk)
            except Gerant.DoesNotExist:
                return Response({"erreur": "gerant introuvable"}, status=status.HTTP_404_NOT_FOUND)
            gerant = {"gerant": data["gerant"]}
            gerant_serializer = GerantSetSerializer(gerant, data=gerant, partial=True)
            if gerant_serializer.is_valid():
                gerant_serializer.save()
                return Response(gerant_serializer.data, status=status.HTTP_200_OK)
            else:
                Response(gerant.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)

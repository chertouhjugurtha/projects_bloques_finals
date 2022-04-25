from rest_framework.response import Response
from .models import Observation
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import ObservationSetSerializer

class ObservationViewSet(APIView):

    def post(self, request):
        
        serializer = ObservationSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        if "observation" in data:
            try:
                observation = Observation.objects.get(id=pk)
            except Observation.DoesNotExist:
                return Response({"erreur": "observation introuvable"}, status=status.HTTP_404_NOT_FOUND)
            observation = {"observation": data["observation"]}
            observation_serializer = ObservationSetSerializer(observation, data=observation, partial=True)
            if observation_serializer.is_valid():
                observation_serializer.save()
                return Response(observation_serializer.data, status=status.HTTP_200_OK)
            else:
                Response(observation.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Observation.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
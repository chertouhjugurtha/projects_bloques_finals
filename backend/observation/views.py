from django.shortcuts import render

# Create your views here.
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
            if observation.is_valid():
                observation_serializer.save()
                return Response(observation_serializer.data, status=status.HTTP_200_OK)
            else:
                Response(observation.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     Observation.objects.filter(circuit_deroutement=pk).update(circuit_deroutement=None, etat_transmission="desactive")
    #     try:
    #         circuit = Observation.objects.prefetch_related(Prefetch("user", to_attr="voie_collecte")).get(id=pk)
    #     except Observation.DoesNotExist:
    #         return Response({"erreur": "element introuvable"}, status=status.HTTP_404_NOT_FOUND)
    #     if circuit.voie_collecte:
    #         #user = User.objects.get(id=circuit.user.id)
    #         user_serializer = UserSerializer(
    #             circuit.voie_collecte,
    #             data={
    #                 "is_collecte": False,
    #                 "circuit": None
    #             },
    #             partial=True)
    #         if user_serializer.is_valid():
    #             user_serializer.save()
    #         else:
    #             print(user_serializer.errors, flush=True)
    #     circuit.delete()
    #     return Response({"reponse": "Element supprimer avec succès"}, status=status.HTTP_204_NO_CONTENT)
    def delete(self, request, pk, format=None):
        snippet = Observation.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
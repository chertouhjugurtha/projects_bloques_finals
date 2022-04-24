from functools import cache
from rest_framework.response import Response
import entreprise
from .models import Entreprise
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import EntrepriseSetSerializer
from rest_framework.decorators import api_view

class EntrepriseViewSet(APIView):

    def post(self, request):
        serializer = EntrepriseSetSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        data=request.data  
        
        try:
            entreprise = Entreprise.objects.get(id=pk)
        except Entreprise.DoesNotExist:
            return Response({"erreur": "entreprise introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['entreprise']=data["entreprise"]
        
        entreprise_serializer = EntrepriseSetSerializer(entreprise, data=data, partial=True)
        if entreprise_serializer.is_valid():
            
            entreprise_serializer.save()
            return Response(entreprise_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(entreprise.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Entreprise.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# import json
# @api_view([ 'POST'])
# def add_entreprise(request):
    
#     with open('code_postal.json', 'r',encoding="utf8") as f:
#         json_objs = json.load(f)
#         # add_new_entreprise()
#         table_json=[]
#         for json_obj in range(len(json_objs)-1):
#             entreprise=json_objs[json_obj]['entreprise_name_ascii']
#             post_code=json_objs[json_obj]['post_code']
#             entreprise=json_objs[json_obj]['entreprise_name_fr']
#             region=json_objs[json_obj]['post_name_ascii']
#             try:
#                 address=json_objs[json_obj]["post_address_entreprise"]
#             except:
#                 address="address invalide"

#             if json_objs[json_obj]['entreprise_name_ascii']!=json_objs[json_obj+1]['entreprise_name_ascii']:
#                 table_json.append({"entreprise":entreprise,"code_postal":post_code,"entreprise":entreprise,"address":address,"region":region,})

#     return Response(table_json)
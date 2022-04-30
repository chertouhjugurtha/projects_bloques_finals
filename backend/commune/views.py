from functools import cache
from rest_framework.response import Response
import commune
from .models import Commune
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import CommuneSetSerializer
from rest_framework.decorators import api_view

class CommuneViewSet(APIView):

    def post(self, request):
        
        serializer = CommuneSetSerializer(data=request.data,many=True)
            # serializer = CommuneSetSerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        data=request.data  
        
        try:
            commune = Commune.objects.get(id=pk)
        except Commune.DoesNotExist:
            return Response({"erreur": "commune introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['commune']=data["commune"]
        
        commune_serializer = CommuneSetSerializer(commune, data=data, partial=True)
        if commune_serializer.is_valid():
            
            commune_serializer.save()
            return Response(commune_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(commune.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = Commune.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
import json
@api_view([ 'GET'])
def get_commune(request):
    
    with open('code_postal.json', 'r',encoding="utf8") as f:
        json_objs = json.load(f)
        # add_new_commune()
        table_json=[]
        for json_obj in range(len(json_objs)-1):
            commune=json_objs[json_obj]['commune_name_ascii']
            post_code=json_objs[json_obj]['post_code']
            # commune=json_objs[json_obj]['commune_name_fr']
            region=json_objs[json_obj]['post_name_ascii']
            try:
                address=json_objs[json_obj]["post_address_commune"]
            except:
                address="address invalide"

            if json_objs[json_obj]['commune_name_ascii']!=json_objs[json_obj+1]['commune_name_ascii']:
                table_json.append({"commune":commune,"code_postal":post_code,"commune":commune,"address":address,"region":region,})

    return Response(table_json)
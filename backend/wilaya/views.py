from functools import partial
from rest_framework.response import Response
from .models import Wilaya
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import WilayaSetSerializer
from rest_framework.decorators import api_view
import json

class WilayaViewSet(APIView):

    def post(self, request):
        serializer = WilayaSetSerializer(data=request.data,many=True)
        # serializer = WilayaSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, code_wilaya):
        data=request.data      
        try:
            wilaya = Wilaya.objects.get(code_wilaya=code_wilaya)
        except Wilaya.DoesNotExist:
            return Response({"erreur": "wilaya introuvable"}, status=status.HTTP_404_NOT_FOUND)
        data['wilaya']=data["wilaya"]
        wilaya_serializer = WilayaSetSerializer(wilaya, data=data, partial=True)
        if wilaya_serializer.is_valid():
            
            wilaya_serializer.save()
            return Response(wilaya_serializer.data, status=status.HTTP_200_OK)
        else:
            Response(wilaya.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "requête mal formée"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, code_wilaya, format=None):
        snippet = Wilaya.objects.get(code_wilaya=code_wilaya)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([ 'GET'])
def get_wilaya(request):
    
    with open('cities_wilaya.json', 'r',encoding="utf8") as f:
        json_objs = json.load(f)
        # add_new_wilaya()
        table_json=[]
        for json_obj in range(len(json_objs)-1):
            wilaya=json_objs[json_obj]['wilaya_name_fr']
            code_wilaya=json_objs[json_obj]['wilaya_code']
        
            if json_objs[json_obj]['wilaya_name_fr']!=json_objs[json_obj+1]['wilaya_name_fr']:
                # continue
                
                table_json.append({"wilaya":wilaya,"code_wilaya":code_wilaya})
    return Response(table_json)
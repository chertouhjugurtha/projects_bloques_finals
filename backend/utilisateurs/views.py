import json
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from debloqueur.models import Debloqueur
from debloqueur.serialisers import DebloqueurSetSerializer

from ministere.models import Ministere
from .serializers import DebloqueurRegistrationSerializer, UserSerializer,SuperUserRegistrationSerializer
from .models import User
import jwt, datetime
from rest_framework import permissions
from rest_framework.authentication import    BasicAuthentication, SessionAuthentication

class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [BasicAuthentication, SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated():
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES) 
        return False

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        debloquer={}
        if 'first_name' in data and 'last_name'in data and'username' in data and  'password' in data and 'is_superviseur' in data['poste_user'] and 'is_user'in data['poste_user'] and 'debloqueur' in data['poste_user'] and "wilaya"in data:
            if data['poste_user']["is_superviseur"]==True:
                data["is_superuser"]=True
                data.pop('poste_user', None)
                
                serializer = SuperUserRegistrationSerializer(data=data)
            elif data['poste_user']["is_user"]==True:
                data["is_user"]=True
                data.pop('poste_user', None)
                serializer = UserSerializer(data=data)
            elif data['poste_user']["debloqueur"]!={}:

                
                # new_group, created = Group.objects.get_or_create(name ='debloqueur')
                # permissions = (
                #     ("add_debloquer_par", "Can change debloquer_ par"),
                #     ("change_debloquer_par", "Can change debloquer_ par"),
                # )
                
                # ct = ContentType.objects.get_for_model(User)
                
                
                # permission = Permission.objects.create(codename ='add_debloquer_par',
                #                                         name ='Debloquer le motifs',
                #                                                 content_type = ct)
                # new_group.permissions.add(permissions)

                data['is_debloqueur']=True
                debloquer=data['poste_user']["debloqueur"]      
                data.pop('poste_user', None)
                 
                serializer = DebloqueurRegistrationSerializer(data=data)
            else:
                return Response({"erreur": "requête mal formée"}, status = status.HTTP_400_BAD_REQUEST)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # insertion debloqueur 
            if debloquer!={}:
                username=data['username']
                utilisateurs=User.objects.get(username=username)
                debloquer['user']=utilisateurs.id
                
                debloquer=DebloqueurSetSerializer(data=debloquer)
                debloquer.is_valid(raise_exception=True)
                debloquer.save()
                # return Response(debloquer.data, status=status.HTTP_201_CREATED)
            return Response({"succes": "utilisateurs à été crier avec succès"}, status=status.HTTP_201_CREATED)
            
        else:
            print('is_superviseur' in data['poste_user']  )
            return Response({"erreur": "requête mal formée"}, status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed('Nom Utilistauer incorrect!')

        if not user.check_password(password):
            raise AuthenticationFailed('Mot de passe incorrect!')
        
        payload = {
            'id': str(user.id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                # .decode('utf-8')
        response = Response()

        response.data = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'wilaya':user.wilaya.wilaya,
            'is_superviseur':user.is_superuser,
            'is_user':user.is_user,
            'is_debloqueur':user.is_debloqueur,
            'token': token
        }
        response.set_cookie(key='token', value=token, httponly=True)
        return response


class UserView(APIView):

    def get(self, request):

        token = request.COOKIES.get('token')

       
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            
            
            payload = jwt.decode(token,'secret' , algorithms=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        payload=uuid.UUID(payload['id']).hex
        user = User.objects.filter(id=payload).first()
        if user.is_superuser:
            serializer = SuperUserRegistrationSerializer(user)
        elif user.is_user:
            serializer = UserSerializer(user)
        elif user.is_debloqueur:
            serializer = DebloqueurRegistrationSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        return response

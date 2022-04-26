import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        phonenumber = request.data['phonenumber']
        password = request.data['password']

        user = User.objects.filter(phonenumber=phonenumber).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                # .decode('utf-8')
        response = Response()
        
        
        # with open('../token.json','w') as json_file:
        #     json.dump({"token":token},json_file)
    
        
        response.data = {
            'jwt': token
        }
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response


class UserView(APIView):

    def get(self, request):
        # return Response()
        # return Response(request.headers)
        token = request.COOKIES.get('jwt')
        # token = request.headers["Cookie"]
       
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            
            # with open('../token.json','w') as json_file:
            #     data=json.dump({"token":token},json_file)
            # jwt.encode(token, 'secret', algorithm='HS256').decode("utf-8")
            # jwt.encode(token, 'secret', algorithms='HS256')
            # jwt.encode(token, "secret", algorithm='HS256').decode('utf-8')
            payload = jwt.decode(token,'secret' , algorithms=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

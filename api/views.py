from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from recipes.models import Recipe
from accounts.models import User
from .serializers import UserSerializer, RecipeSerializer

import jwt, datetime

@api_view(['GET'])
def getRoutes(request):
    routes = [

        '/api/recipes/',
    ]
    return Response(routes)

@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') # TODO: replace hardcoded secret

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = ({
            'jwt': token
        })
        
        return response
    
class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Not authenticated!")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256']) # TODO: replace hardcoded secret
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Expired signature error!")
        
        # user = User.objects.get(payload['id'])
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)


        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        # Remove JWT cookie
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
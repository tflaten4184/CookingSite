from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

from recipes.models import Recipe
from .serializers import UserSerializer, RecipeSerializer

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
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.models import Recipe
from .serializers import RecipeSerializer

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
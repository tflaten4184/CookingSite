from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

from accounts.models import User
from .models import Recipe, UserFavoriteRecipe

def index(request):
    recipes_list = Recipe.objects.order_by("-id")[:5]
    template = loader.get_template("recipes/index.html")
    context = {
        "recipes_list": recipes_list,
    }
    
    return HttpResponse(template.render(context, request))

def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    template = loader.get_template("recipes/detail.html")
    user = User.objects.get(username=request.user)

    is_favorite = UserFavoriteRecipe.objects.filter(user=user, recipe=recipe_id)

    context = {
        "recipe": recipe,
        "is_favorite": is_favorite,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template("recipes/create.html")
    return HttpResponse(template.render(request))

def favorite_recipe(request, recipe_id):
    print("in favorite_recipe")

    user = User.objects.get(username=request.user.username)
    recipe = Recipe.objects.get(id=recipe_id)

    # Create UserFavoriteRecipe
    if user: # Currently authenticated user is not None
        new_favorite = UserFavoriteRecipe(user=user, recipe=recipe)
        print(new_favorite)
        new_favorite.save()

    return redirect('.')

# Similar to favorite_recipe, but for AJAX
@ login_required
def post_favorite_recipe(request, recipe_id):
    print(f"in post_favorite_recipe, recipeId is {recipe_id}")
    print(request.POST)
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('recipeId'))
        # user = User.objects.get(username=request.user.username)
        user = get_object_or_404(User, username=request.user.username)
        recipe = Recipe.objects.get(id=recipe_id)

        # Create UserFavoriteRecipe
        if user: # Currently authenticated user is not None
            new_favorite = UserFavoriteRecipe(user=user, recipe=recipe)
            print(new_favorite)
            new_favorite.save()

    return JsonResponse({"success":True})

def unfavorite_recipe(request, recipe_id):

    user = request.user

    # Find the object that relates the user to the recipe, and remove that relationship (destroy the association object)
    if user: # Currently authenticated user is not None
        if recipe_id:            
            UserFavoriteRecipe.objects.get(user=request.user.id, recipe=recipe_id).delete()

    return redirect('.')

# AJAX version of unfavorite_recipe
@ login_required
def post_unfavorite_recipe(request, recipe_id):

    user = request.user

    # Find the object that relates the user to the recipe, and remove that relationship (destroy the association object)
    if user: # Currently authenticated user is not None
        if recipe_id:            
            UserFavoriteRecipe.objects.get(user=request.user.id, recipe=recipe_id).delete()

    return JsonResponse({"success":True})

    
def favorites(request):

    template = loader.get_template("recipes/favorites.html")

    user = User.objects.get(username=request.user.username)
    favorites_list = UserFavoriteRecipe.objects.filter(user=user.id)
    print(f"favorites list: {favorites_list}")
    recipes_list = []
    for favorite in favorites_list:
        current_recipe = Recipe.objects.get(id=favorite.recipe.id)
        print(f"current_recipe: {current_recipe}")
        recipes_list.append(current_recipe)
    print(recipes_list)

    context = {
        "recipes_list": recipes_list
    }

    return HttpResponse(template.render(context, request))



from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
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

#     # We want to create a relationship between the authenticated user and the recipe on the current page.
#     # This should only be called from the recipe detail page.
#     # Technically, we can do this using Django forms. The "Favorite" button will trigger the submission
#     # to create a new instance of the model UserFavoriteRecipe

    user = User.objects.get(username=request.user.username)
    recipe = Recipe.objects.get(id=recipe_id)

    # Create UserFavoriteRecipe
    if user: # Currently authenticated user is not None
        new_favorite = UserFavoriteRecipe(user=user, recipe=recipe)
        print(new_favorite)
        new_favorite.save()

    return redirect('.')

def unfavorite_recipe(request, recipe_id):

    user = request.user

    # Find the object that relates the user to the recipe, and remove that relationship (destroy the association object)
    if user: # Currently authenticated user is not None
        # Find matching "Favorite" object, based on current user and recipe ID
        # Delete the target Favorite object
        if recipe_id:
            print(f"favorite = {recipe_id}")
            
            UserFavoriteRecipe.objects.get(user=request.user.id, recipe=recipe_id).delete()
        # Show some feedback to confirm success
        pass

    return redirect('.')
    
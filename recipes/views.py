from django.template import loader
from django.http import HttpResponse
from .models import Recipe

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
    context = {
        "recipe": recipe,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template("recipes/create.html")
    return HttpResponse(template.render(request))
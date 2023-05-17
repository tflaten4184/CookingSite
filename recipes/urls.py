from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.detail, name="detail"),
    path("<int:recipe_id>/favorite", views.favorite_recipe, name="favorite"),
    path("<int:recipe_id>/unfavorite", views.unfavorite_recipe, name="unfavorite"),
]

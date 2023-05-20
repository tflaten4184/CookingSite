from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.detail, name="detail"),
    path("favorites", views.favorites, name="favorites"),
    path("<int:recipe_id>/favorite", views.favorite_recipe, name="favorite"),
    path("<int:recipe_id>/unfavorite", views.unfavorite_recipe, name="unfavorite"),
    path("<int:recipe_id>/favorite_ajax", views.post_favorite_recipe, name="favorite_ajax"),
    path("<int:recipe_id>/unfavorite_ajax", views.post_unfavorite_recipe, name="unfavorite_ajax"),

]

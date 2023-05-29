from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
]

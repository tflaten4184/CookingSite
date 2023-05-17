from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Step, User, UserFavoriteRecipe


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ['ingredient']

class StepInline(admin.TabularInline):
    model = Step

class UserAdmin(admin.ModelAdmin):
    model = User

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, StepInline]
    list_display = ('name', 'ingredient_list', 'step_list')

    def ingredient_list(self, obj):
        return ", ".join([recipe_ingredient.ingredient.name for recipe_ingredient in obj.recipe_ingredients.all()])
    
    def step_list(self, obj):
        return ", ".join([step.text[:15]+"..." for step in obj.steps.all()])

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class UserFavoriteRecipeAdmin(admin.ModelAdmin):
    model = UserFavoriteRecipe

admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(UserFavoriteRecipe, UserFavoriteRecipeAdmin)
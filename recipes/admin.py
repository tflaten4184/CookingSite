from django.contrib import admin
from .models import Recipe, Ingredient, Step

class IngredientInline(admin.TabularInline):
    model = Ingredient

class StepInline(admin.TabularInline):
    model = Step

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]
    list_display = ('name', 'ingredient_list', 'step_list')

    def ingredient_list(self, obj):
        return ", ".join([ingredient.name for ingredient in obj.ingredients.all()])
    
    def step_list(self, obj):
        return ", ".join([step.text[:15]+"..." for step in obj.steps.all()])


admin.site.register(Recipe, RecipeAdmin)
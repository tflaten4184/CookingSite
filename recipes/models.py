from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from .ConversionUtil import ConversionUtil
from accounts.models import User

User = get_user_model()

class Recipe(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    # For later, other fields:
    # Author?
    # Link?
    # Category?
    # Food restriction? (in Ingredient instead?)

    @property
    def calculated_cost(self):

        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.id)
        total = Decimal(0)
        for ing in recipe_ingredients:
            total += Decimal(ing.calculated_cost)
        return total

    def __str__(self):
        return f"Recipe for {self.name}, costs {self.calculated_cost}"
    
class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    base_unit = models.CharField(max_length=100, null=True, blank=True)
    base_price = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self) -> str:
        return f"{self.name}: {self.base_unit} at {self.base_price}"
    
class RecipeIngredient(models.Model):
    
    quantity = models.DecimalField(decimal_places=2, max_digits=1000)
    unit = models.CharField(max_length=100, null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients") # many to one

    
    @property
    def calculated_cost(self):
        return Decimal(ConversionUtil.convert_ingredient_to_dollars(self, self.ingredient)).quantize(Decimal('.01'), rounding="ROUND_UP")


    def __str__(self) -> str:
        return f"RecipeIngredient {self.ingredient.name} for Recipe {self.recipe.name} at cost {self.calculated_cost}"
    

class Step(models.Model):

    number = models.SmallIntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps") # many to one

    def __str__(self) -> str:
        return f"Step {self.number} of recipe {self.recipe}: {self.text[:30]}"
    
class UserFavoriteRecipe(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"User {self.user} favorites recipe {self.recipe}"

    class Meta:
       unique_together = ('user', 'recipe',)
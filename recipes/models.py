from decimal import Decimal
from django.db import models
from pint import UnitRegistry
from . import ConversionUtil

class Recipe(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    # For later, other fields:
    # Steps? (list of "step" objects, or just a simple string for now)
    # Author?
    # Link?

    @property
    def calculated_cost(self):
        # TODO:
        # Get collection of all RecipeIngredients and total up the calculated_cost all, using related_manager as a reverse reference. *********************
        print("in function calculated_cost")
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self.id)
        print(recipe_ingredients)
        total = Decimal(0)
        for ing in recipe_ingredients:
            print(ing.calculated_cost)
            total += Decimal(ing.calculated_cost)
        return total

    def __str__(self):
        return f"Recipe for {self.name}, costs {self.calculated_cost}"
    
class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    base_unit = models.CharField(max_length=100)
    base_price = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self) -> str:
        return f"{self.name}: {self.base_unit} at {self.base_price}"
    
class RecipeIngredient(models.Model):
    
    # name = models.CharField(max_length=100)
    quantity = models.DecimalField(decimal_places=2, max_digits=1000)
    unit = models.CharField(max_length=100)
    # calculated_cost = models.FloatField() # ***** (derived value)
    # Need: two foreign keys
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients") # many to one

    
    @property
    def calculated_cost(self):
        # ?Use related_manager (reverse reference) to get base unit and cost per base unit?
        # Convert recipe's quantity and unit to base unit
        # Multiply to get cost for this RecipeIngredient
        return Decimal(ConversionUtil.ConversionUtil.convert_ingredient_to_dollars(self, self.ingredient)).quantize(Decimal('.01'), rounding="ROUND_UP")


    def __str__(self) -> str:
        return f"RecipeIngredient {self.ingredient.name} for Recipe {self.recipe.name} at cost {self.calculated_cost}"
    

class Step(models.Model):

    number = models.SmallIntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps") # many to one

    def __str__(self) -> str:
        return f"Step {self.number} of recipe {self.recipe}: {self.text[:30]}"
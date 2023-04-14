from django.db import models

class Recipe(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField()

    # For later, other fields:
    # Image?
    # Steps? (list of "step" objects, or just a simple string for now)
    # Author?
    # Link?

    def __str__(self):
        return f"Recipe for {self.name}"
    
class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    quantity = models.DecimalField(decimal_places=2, max_digits=1000)
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients") # many to one

    def __str__(self) -> str:
        return f"{self.quantity.normalize()} {self.unit} {self.name}"
    
class Step(models.Model):

    number = models.SmallIntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps") # many to one

    def __str__(self) -> str:
        return f"Step {self.number} of recipe {self.recipe}: {self.text[:30]}"
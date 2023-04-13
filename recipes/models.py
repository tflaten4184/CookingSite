from django.db import models

class Recipe(models.Model):

    title = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)

    # For later, other fields:
    # Image?
    # Steps? (list of "step" objects, or just a simple string for now)
    # Author?
    # Link?

    def __str__(self):
        return f"Recipe for {self.title}"
    

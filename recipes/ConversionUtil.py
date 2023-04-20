# The purpose of this script is to play around with "pint" module to understand how it works.

# First, let's do volume.
# For now, assume our base unit will be "cups".

from decimal import Decimal
from pint import UnitRegistry

class ConversionUtil():

    print("Initializing UnitRegistry")
    ureg = UnitRegistry()
    
    def convert_ingredient_to_dollars(recipeIngredient, ingredient):

        # First, need to check if the unit is nontraditional (for example, "1 whole onion")
        if ingredient.base_unit == "whole":
            return float(recipeIngredient.quantity) * float(ingredient.base_price)

        ureg = ConversionUtil.ureg

        # 1) Parse input unit, quantity
        input_measure = ureg(f"{str(recipeIngredient.quantity) + recipeIngredient.unit}")

        # 2) Convert input unit to base unit, then multiply by rate
        converted_price = input_measure.to(ureg(ingredient.base_unit)).magnitude * float(ingredient.base_price)

        return Decimal(converted_price)


# These classes are only used for testing the function
class Ingredient():
    def __init__(self, base_price, base_unit) -> None:
        self.base_price = base_price
        self.base_unit = base_unit

class RecipeIngredient():
    def __init__(self, quantity, unit) -> None:
        self.quantity = quantity
        self.unit = unit



if __name__ == "__main__":
        
    # Test case: typical unit conversion

    test_ingredient = Ingredient(3.10, "gal")
    test_recipeIngredient = RecipeIngredient(2, "cup")

    cost = ConversionUtil.convert_ingredient_to_dollars(test_recipeIngredient, test_ingredient)
    print(cost)


    # Test case: nontraditional unit ("whole onion")
    test_ingredient = Ingredient(0.69, "whole")
    test_recipeIngredient = RecipeIngredient(2, "whole")

    cost = ConversionUtil.convert_ingredient_to_dollars(test_recipeIngredient, test_ingredient)
    print(cost)
# The purpose of this script is to play around with "pint" module to understand how it works.

# First, let's do volume.
# For now, assume our base unit will be "cups".

from pint import UnitRegistry

class ConversionUtil():

    print("Initializing UnitRegistry")
    ureg = UnitRegistry()

    # def convert_ingredient_to_dollars(input_quantity, input_unit, base_price, base_unit):

    #     # 1) Parse input unit, quantity
    #     input_measure = ureg(f"{str(input_quantity) + input_unit}")

    #     # 2) Convert input unit to base unit
    #     converted_price = input_measure.to(ureg(base_unit)).magnitude * base_price

    #     return converted_price
    
    def convert_ingredient_to_dollars(recipeIngredient, ingredient):

        ureg = ConversionUtil.ureg

        # 1) Parse input unit, quantity
        input_measure = ureg(f"{str(recipeIngredient.quantity) + recipeIngredient.unit}")

        # 2) Convert input unit to base unit, then multiply by rate
        converted_price = input_measure.to(ureg(ingredient.base_unit)).magnitude * ingredient.base_price

        return converted_price

class Ingredient():
    def __init__(self, base_price, base_unit) -> None:
        self.base_price = base_price
        self.base_unit = base_unit

class RecipeIngredient():
    def __init__(self, quantity, unit) -> None:
        self.quantity = quantity
        self.unit = unit



if __name__ == "__main__":
        
    # Initialize ingredient and recipeIngredient

    test_ingredient = Ingredient(3.10, "gal")
    test_recipeIngredient = RecipeIngredient(2, "cup")

    cost = ConversionUtil.convert_ingredient_to_dollars(test_recipeIngredient, test_ingredient)
    print(cost)
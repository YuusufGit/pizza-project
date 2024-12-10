from src.v2.pizza import Pizza

class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.base = pizza
        self.toppings = self.base.toppings + ['pepperoni']  # Merge toppings with base

    def is_veggetarian(self):
        return False

    def calculate_price(self):
        return 1.5 + self.base.calculate_price()

    def is_dairy_free(self):
        return self.base.is_dairy_free()

    def remove_topping(self, topping_class):
        # If this layer is the topping to remove
        if isinstance(self, topping_class):
            # Skip this layer and recursively call on the base
            return self.base.remove_topping(topping_class)
        else:
            # Otherwise, propagate removal to the base
            self.base = self.base.remove_topping(topping_class)
            self.toppings = self.base.toppings  # Sync toppings with base
            return self


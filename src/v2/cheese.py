from src.v2.pizza import Pizza

class Cheese(Pizza):
    def __init__(self, pizza):
        self.base = pizza
        self.toppings = pizza.toppings + ['cheese']
    def is_veggetarian(self):
        return self.base.is_veggetarian()

    def calculate_price(self):
        return 1.0 + self.base.calculate_price()

    def is_dairy_free(self):
        return False

    def remove_topping(self, pizza_class):
        if isinstance(self, pizza_class):
            return self.base.remove_topping(pizza_class)
        else:
            self.base = self.base.remove_topping(pizza_class)
            return self






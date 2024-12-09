# from src.v2.pizza import Pizza

# class BlackOlive(Pizza):
#     def __init__(self, pizza):
#         self.base = pizza

#     def is_veggetarian(self):
#         return self.base.is_veggetarian()

#     def calculate_price(self):
#         return 1.0 + self.base.calculate_price()

#     def is_dairy_free(self):
#         return self.base.is_dairy_free()

#     def remove_topping(self, pizza_class):
#         if isinstance(self, pizza_class):
#             return self.base.remove_topping(pizza_class)
#         else:
#             self.base = self.base.remove_topping(pizza_class)
#             return self

from src.v2.pizza import Pizza

class BlackOlive(Pizza):
    def __init__(self, pizza):
        self.base = pizza
        self.toppings = self.base.toppings + ['black olive'] if hasattr(self.base, 'toppings') else ['black olive']

    def is_veggetarian(self):
        return self.base.is_veggetarian()

    def calculate_price(self):
        return 1.0 + self.base.calculate_price()

    def is_dairy_free(self):
        return self.base.is_dairy_free()

    def remove_topping(self, pizza_class):
        if isinstance(self, pizza_class):
            return self.base.remove_topping(pizza_class)
        else:
            self.base = self.base.remove_topping(pizza_class)
            self.toppings = self.base.toppings  # Sync toppings with base pizza
            return self



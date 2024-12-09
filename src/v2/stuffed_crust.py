from src.v2.pizza import Pizza

# class StuffedCrust(Pizza):
#     def is_veggetarian(self):
#         return True

#     def calculate_price(self):
#         return 8

#     def is_dairy_free(self):
#         return True

class StuffedCrust(Pizza):
    def __init__(self):
        self.toppings = []

    def is_veggetarian(self):
        return True

    def calculate_price(self):
        return 8

    def is_dairy_free(self):
        return True

    def remove_topping(self, topping_class):
        # Base pizza has no layers to remove
        return self

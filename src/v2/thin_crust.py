# from src.v2.pizza import Pizza

# class ThinCrust(Pizza):
#     def is_veggetarian(self):
#         return True
#     def calculate_price(self):
#         return 8.0


from src.v2.pizza import Pizza

class ThinCrust(Pizza):
    def __init__(self):
        self.toppings = ['thin']

    def is_veggetarian(self):
        return True

    def calculate_price(self):
        return 8.0

    def remove_topping(self, topping_class):
        # If the topping class matches ThinCrust, return None (base case for decoration removal)
        if isinstance(self, topping_class):
            return None
        # Otherwise, return self as there is no topping to remove in ThinCrust
        return self

crusts = {'thin', 'deepdish', 'hand_tossed', 'stuffed'}
toppings = {'cheese', 'sausage', 'black_olive', 'pepperoni'}
meats = {'sausage', 'pepperoni'}
prices = {'thin': 8.0,
          'deepdish': 8.0,
          'hand_tossed': 8.0,
          'stuffed': 8.0,
          'cheese': 1.0,
          'sausage': 1.5,
          'black_olive': 1.0,
          'pepperoni': 4.0}

def make_pizza(crust):
    if crust not in crusts:
        raise AttributeError('Invalid crust: ' + str(crust))
    return {'crust': crust, 'toppings': []}

def get_crust(pizza):
    return pizza['crust']

def get_toppings(pizza):
    return pizza['toppings']

def add_topping(pizza, topping):
    if topping not in toppings:
        raise AttributeError('Invalid topping: ' + str(topping))
    get_toppings(pizza).append(topping)

def is_veggetarian(pizza):
    return not (meats & set(get_toppings(pizza)))

def calculate_price(pizza):
    total_price = prices[get_crust(pizza)]
    for topping in get_toppings(pizza):
        total_price += prices[topping]
    return total_price

# def remove_topping(pizza, topping):
#     pizza['toppings'] = [t for t in pizza['toppings'] if t != topping]

def remove_topping(pizza, topping):
    pizza['toppings'] = [t for t in pizza['toppings'] if t != topping]


def is_dairy_free(pizza):
    return 'cheese' not in get_toppings(pizza)




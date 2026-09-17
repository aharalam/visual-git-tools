cart = []

def get_total():
    return sum(item['price'] * item['quantity'] for item in cart)

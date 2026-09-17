cart = []

def get_total():
    # Calculate the total price of items in the cart:
    return sum(item['price'] * item['quantity'] for item in cart)

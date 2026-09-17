cart = []

def get_total():
    # Calculate the total price of items in the cart:
    return sum(item['price'] * item['quantity'] for item in cart)

def clear_cart():
    # Clear the cart by emptying the list:
    cart.clear()
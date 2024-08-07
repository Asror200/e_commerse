from django.contrib import messages


class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if cart is None:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def checkout(self, product_id):
        if str(product_id) in self.cart:
            return False
        return True

    def add(self, product):
        product_id = str(product.id)
        self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

    def get_cart_items(self):
        return self.cart

    def product_quantity(self):
        return len(self.cart)

from decimal import Decimal
from django.conf import settings
from .models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID, {})

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        self.cart[product_id] = {
            'quantity': quantity if override_quantity else (self.cart.get(product_id, {}).get('quantity', 0) + quantity),
            'price': str(product.price)
        }
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

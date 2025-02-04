from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if quantity > product.quantity:
            print(f"Not available '{product.name}'! Available: {product.quantity}.")
        else:
            self.cart_items.append((product, quantity))
            product.update_quantity(product.quantity - quantity)
            print(f"Added {quantity} pcs. product '{product.name}' in cart.")

    def total_cart_value(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("\nProducts in cart:")
            for product, quantity in self.cart_items:
                print(f"{product.name} - {quantity} pcs. - {product.price * quantity}")
            print(f"\nTotal sum: {self.total_cart_value()}")

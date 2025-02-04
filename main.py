from product import Product
from product_manager import ProductManager
from cart import Cart

#kreiranje instance
manager = ProductManager()
cart = Cart()

#dodavanje proizvoda
product1 = (Product("TV", 1000, 6))
product2 = (Product("Laptop", 600, 10))
product3 = (Product("Phone", 350, 15))

manager.add_products(product1)
manager.add_products(product2)
manager.add_products(product3)

#lista proizvoda
print("List of product:")
manager.display_products()

#dodavanje proizvoda u korpu
cart.add_to_cart(product1,2)
cart.add_to_cart(product2,1)

#prikaz korpe
cart.display_cart()

#ukupna vrednost
print(f"Total sum:{manager.total_value()}")





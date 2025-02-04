from product import Product
from product_manager import ProductManager

#kreiranje instance
manager = ProductManager()

#dodavanje proizvoda
manager.add_products(ProductManager("TV", 1000, 6))
manager.add_products(ProductManager("Laptop", 600, 10))
manager.add_products(ProductManager("Phone", 350, 15))

#lista proizvoda
print("List of product:")
manager.display_products()

#ukupna vrednost
print(f"Total sum:{manager.total_value()}")



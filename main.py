from product import Product
from product_manager import ProductManager

#kreiranje instance
manager = ProductManager()

#dodavanje proizvoda
manager.add_products(ProductManager("TV", 1000, 10))
manager.add_products(ProductManager("Laptop", 600, 10))
manager.add_products(ProductManager("Phone", 350, 7))





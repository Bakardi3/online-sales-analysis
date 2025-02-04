from product import Product

class ProductManager(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name,price,quantity)
        self.products = []


    def add_products(self,product):
        self.products.append(product)
        print(f"Product ({self.name}) is added.")

    def display_products(self):
        if not self.products:
            print("No available products.")
        else:
            print(f"Product:{self.name}-price{self.price}-quantity-{self.quantity}")
                

    def total_value(self):
        total = sum(self.price * self.quantity for self.name in self.products)
        print(f"Total sum:{total}")
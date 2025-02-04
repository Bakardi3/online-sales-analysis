class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product name:{self.name}-price:{self.price}-quantity({self.quantity})")

    def update_quantity(self,new_quantity):
        self.quantity = new_quantity
        print(f"Product-{self.name},has updated qunatity:{self.quantity}")
        
        
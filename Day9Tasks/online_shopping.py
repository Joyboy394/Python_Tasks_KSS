class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}, Price: {self.price}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} years")


class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, battery_capacity):
        super().__init__(name, price, warranty)
        self.battery_capacity = battery_capacity

    def display(self):
        super().display()
        print(f"Battery Capacity: {self.battery_capacity} mAh")


phone1 = MobilePhone("iPhone 16", 79999, 1, 3349)

print("Product Details:")
phone1.display()

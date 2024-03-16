class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity
    
class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        

class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        
class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))

    def calculate_total_bill(self):
        total_bill = 0
        for item, quantity in self.items:
            total_bill += item.calculate_total_price(quantity)
        return total_bill
    
# Menu
water = Beverage("Agua", 2.5)
coke = Beverage ("Sprite", 2.7)
coke2 = Beverage("CocaCola", 3.0)
vino = Beverage("Vino Tinto", 60.0)
vino2 = Beverage("Vino Blanco", 55.0)

wings = Appetizer("Alitas BBQ", 14.0)
wings2 = Appetizer("Alitas bufalo", 15.5)
wings3 = Appetizer("Alitas rellenas", 18.2)
wings4 = Appetizer("Alitas Ranch", 12.5)

pasta = MainCourse("Pasta Carbonara", 25.2)
pasta2 = MainCourse("Pasta Pesto", 24.0)
pasta3 = MainCourse("Pasta Boloñesa", 25.5)
pasta4 = MainCourse("Pasta con camarones", 26.0)  


my_order = Order ()
my_order.add_item(coke2, 2)
my_order.add_item(coke, 1)
my_order.add_item(wings, 3)
my_order.add_item(pasta, 1)
my_order.add_item(pasta2, 2)
total_amount = my_order.calculate_total_bill()
print(f"Total bill amount: ${total_amount:.2f}")


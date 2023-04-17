class Item:
    #Class attribute
    pay_rate = 0.8  #After 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation to received arguments
        assert price>=0, f"Price {price} is negative"   #Helps with bugs
        assert quantity>=0, f"Price {price} is negative"
        #Assign to self
        self.name=name
        self.price = price
        self.quantity = quantity
        print(f"Created")

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  #Do not use Item.pay_rate
item1 = Item("Phone", 100 , 5)
#print(item1.calculate_total_price(item1.price,item1.quantity))

item2 = Item("Laptop", 1000, 3)
item2.has_numpy = False
print(Item.pay_rate)
#print(Item.__dict__)    #All attributes at class lvl
#print(item1.__dict__)
item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
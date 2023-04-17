class Item:
    #Class attribute
    pay_rate = 0.8  #After 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation to received arguments
        assert price>=0, f"1.Price {price} is negative"   #Helps with bugs
        assert quantity>=0, f"2.Price {price} is negative"
        #Assign to self
        self.name=name
        self.price = price
        self.quantity = quantity
        print(f"3. Created")
        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  #Do not use Item.pay_rate

    def __repr__(self):
        return f"4.Item('{self.name}', {self.price},{self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:   #Check
    print(instance.name)
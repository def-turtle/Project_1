class Item:
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = price
        self.description = description
        self.size = size
class Buyer:
    def __init__(self, name, surname, email, phone_number):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
class Cart:
    def __init__(self, buyer):
        self.buyer = buyer
        self.items = {}
    def add(self, item, count=1):
        self.items[item.name] = f"Price: {item.price}, Amount: {count}, Description: {item.description}, Size: {item.size}"
        print(self.items)
banana = Item("Banana","13", "yellow", "big")
user = Buyer("Me","surname", "me@gmail.com", "+6874512384")
cart = Cart(user)
cart.add(banana)
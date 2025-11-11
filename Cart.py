class Item:
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = int(price)
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
        self.items[item.name] = {
            "price": item.price, "amount": count, "description": item.description, "size": item.size
        }
        print(self.items)
    def get_total_price(self):
        total_price = 0
        for i in self.items.values():
            total_price += i['price'] * i['amount']
        print("Total Price: ", total_price)
banana = Item("Banana","13", "yellow", "big")
carrot = Item("Carrot","13", "yellow", "small")
user = Buyer("Me","surname", "me@gmail.com", "+6874512384")
cart = Cart(user)
cart.add(banana)
cart.add(carrot)
cart.get_total_price()
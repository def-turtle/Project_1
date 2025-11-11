class Animal:

    @staticmethod
    def sound(self):
        print('Animal')
class Dog(Animal):
    @staticmethod
    def sound(self):
        print('Woof')
dog1 = Dog()
dog1.sound()
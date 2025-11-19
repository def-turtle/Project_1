import math
class CatchError(Exception):
    pass
class Cat:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        return f'{self.name} is {self.age} years old'

    def __getattr__(self, atr_name):
        return "error"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __delattr__(self, key):
        print("removed object:", key)
        del self.__dict__[key]

    name = property() # Створення властивості name без методів контролю

    @name.getter
    def name(self):
        print("call get name")
        return self.__name

    @name.setter
    def name(self, name_value):
        print("call set name")
        self.__name = name_value

    @name.deleter
    def name(self):
        print("call remove name")
        del self.__name
cat = Cat("Jerry", 12)
# # print(cat)
# # print(cat.supercool)
# print(getattr(cat, 'supercool'))
# print(getattr(cat, 'name'))
# atr1 = getattr(math, 'pow')
# print(int(atr1(2,2)))
#

dict1 = {"type":"Good", "gender":"male"}
for key,val in dict1.items():
    setattr(cat, key, val)
print(cat.gender)
delattr(cat, "gender")
print(cat.gender)
del cat.type
print(cat.type)
# print(getattr(cat,"no"))
# list1 = ['age',"name","hello"]
# for i in list1:
#     if hasattr(cat,i):
#         print(getattr(cat,i))
#     else:
#         print("False")

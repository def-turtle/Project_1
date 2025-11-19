# class Coordinate:
#
#     def __init__(self):
#         self.value = None
#
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         self.value = value
#     def __delete__(self, instance):
#         del self.value
#
# class Point:
#     x = Coordinate()
#     y = Coordinate()
#
#
# point = Point()
# print(point.x, point.y) # виведе None None
#
# point.x = 50
# point.y = 20
# del point.x
# print(point.x, point.y) # виведе 50 20
slice1 = slice(0,3)
a = [1,2,3,4,5]
print(a[slice1])
print(a[0:3])
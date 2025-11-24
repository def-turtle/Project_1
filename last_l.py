# lst = [1,2,3,4,5]
# a = iter(lst)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# try:
#     print(next(a))
# except StopIteration:
#     print("StopIteration")
# a = "Hello World"
# b = a.__iter__()
# print(type(b))
# a = (1,2)
# b = a.__iter__()
# print(type(b))
# a = (1,2)
# b = a.__iter__()
# b.__next__()
# print(b.__next__())
a = {10,20}
b = iter(a)
print(next(b))
print(next(b))
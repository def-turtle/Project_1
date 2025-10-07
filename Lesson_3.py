# print(bool(1))
# print(bool(5))
# print(bool(0))
# print(bool(None))
# number_b = 7
# number_a = 8
# z = 10 if number_b > number_a else number_b
# a = None
# b = 23
# c = b or a
# z = a if b < c else 10
# print(bool(c))
# print(z)
# example= [1,2,3]
# example.append(4)
# print(example)
# print(example[0])
# examplelist = list()
# print(examplelist)
# a = [1,2,[1,2,3]]
# print(a[-1])
# a.append([4,5,6])
# print(a[-1])
# a[0]='hello'
# print(a)
# a.insert(1,2)
# print(a)
# a = [1,2,3,4,5]
# a.insert(1,5)
# print(a)
# a.remove(5)
# print(a)
# x = a.pop(1)
# b = a[1]
# print(a)
# print(x)
# print(b)
# del a[3]
# print(a)
# a.append(6)
# print(a)
lst = [1,2,3,4,5,6,7,8,9]
if 5 in lst:
    print("5 is in lst")
else:
    print("5 is not in lst")
lst.remove(5)
if 5 in lst:
    print("5 is in lst")
else:
    print("5 is not in lst")
len1 = len(lst)
acc_len1 = len1+1
print(acc_len1)
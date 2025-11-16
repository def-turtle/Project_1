def prime_generator(number):
    list1 = []
    prime_list = [2]
    for i in range(1,number+1):
        list1.append(i)
    a = False
    yield 2
    for i in list1:
        if i == 1:
            continue
        for l in range(2,i):
            if i % l == 0:
                a = False
                break
            else:
                a = True

        if a == True:
            yield i
    if number == 1:
        # print(True)
        return True
    else:
        # print(prime_list)
        return prime_list
from inspect import isgenerator
# prime_generator(29)
# print(list(prime_generator(10)))
gen = prime_generator(10)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
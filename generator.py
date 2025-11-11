def pow1(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності

    """
    # list1 = []
    # for i in range(end):
    #     if len(list1)==0:
    #         list1.append(begin)
    #         continue
    #     last_item = list1[-1]
    #     list1.append(func(last_item))
    # print(list1)
    beginning = begin
    for i in range(end):
        yield beginning
        beginning  =  func(beginning)
gen = some_gen(2, 4, pow1)
from inspect import isgenerator

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

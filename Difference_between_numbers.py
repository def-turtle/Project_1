
def difference(*args):
    if len(args) == 0:
        print("0")
        return 0

    else:
        max_item = max(list(args))
        min_item = min(list(args))
        difference1 = max_item - min_item

        if type(difference1) == int:
            print(difference1)
            return difference1

        else:
            difference1 = round(difference1,2)
            print(difference1)
            return difference1

difference()

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
def find_unique_value(some_list:list):
    unique_item = 0
    for item in some_list:
        if some_list.count(item)==1:
            unique_item = item
        else:
            pass
    print(unique_item)
    return unique_item
find_unique_value([1,2,1,1])
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([2,2,2]) == 0, 'Test4'
print("ОК")
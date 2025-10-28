def add_one(some_list):
    int_result = int(''.join(map(str, some_list)))+1
    new_list = list(map(int, str(int_result)))
    return new_list
    print(new_list)

add_one([1,2,3,4])

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

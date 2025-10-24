def second_index(user_input="Hello_World",letter1='a'):
    found_1 = user_input.find(letter1)
    # print(found_1)
    count1 = user_input.count(letter1)
    # print(count1)
    if found_1 != -1:
        if count1 <2:
            print("Found it: ", found_1)
            return None
        user_list = user_input[found_1+1:]
        user_input = user_input[:found_1+1]
        user_input_c = len(user_input)
        # print(user_input_c)
        # print(user_input)
        # print(user_list)
        print("Found it: ", user_list.find(letter1)+user_input_c)
        return user_list.find(letter1)+user_input_c
    else:
        print("Not Found")
second_index("simsdfsims","sims")
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
#
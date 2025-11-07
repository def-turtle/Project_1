def is_even(number):
    list1 = list(map(int, str(number)))
    if list1[-1] == 2 or list1[-1] == 4 or list1[-1] == 6 or list1[-1] == 8 or list1[-1] == 0:
        print("Even")
        return True
    else:
        print("Odd")
        return False
is_even(3494563894035**2)
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
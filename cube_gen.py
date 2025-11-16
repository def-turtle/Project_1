def generate_cube_numbers(number):
    list1 = []
    for i in range(number):
        list1.append(i)
    list1.remove(0)
    list1.remove(1)
    for i in list1:
        if i**3 <= number:
            yield i**3
# print(list(generate_cube_numbers(10)))
from inspect import isgenerator
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")
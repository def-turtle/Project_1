import string
alphabet = string.ascii_letters
alphabet_l = list(alphabet)
print(alphabet_l)
user_input = input("Please input two letters like this: a-c: ")
first_letter = user_input[0]
second_letter = user_input[2]
first_index = alphabet.index(first_letter)
second_index = alphabet.index(second_letter)
cut = alphabet_l[first_index:second_index+1]
answear = ''.join(cut)  #інфо з цього сайту: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

print(answear)
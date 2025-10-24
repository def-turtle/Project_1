def correct_sentence(text:str):
    if len(text) == 0:
        return ''
    else:
        text = text[0].upper() + text[1:]
        if text[-1]==".":
            return text
        else:
            return text + '.'
    # first_wrd = first_wrd[0].upper()+first_wrd[1:].lower()
    # second_lst = list(second_wrd)
    # if len(second_lst) == 0:
    #     print(first_wrd)
    #     return first_wrd
    # elif second_lst[-1]==".":
    #     print(first_wrd, second_wrd)
    #     return first_wrd,second_wrd
    # else:
    #     b = first_wrd," ", second_wrd, "."
    #     c = ''.join(b)
    #     print(c)
    #     return c
#correct_sentence("greetings,","friends")
# a = correct_sentence("greetings","friends")
# print(a)
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
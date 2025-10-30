import string
def is_palindrome(text:str):
    banned = string.punctuation
    for i in banned:
        if i in text:
            text = text.replace(i,"")
    if " " in text:
        text = text.replace(" ","")
    text = text.lower()
    text_l = list(text)
    if text_l[::-1] == list(text):
       return True
    else:
        return False
is_palindrome('A man, a plan, a canal: Panama')
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert not is_palindrome('aurora') == True, 'Test4'
print("ОК")
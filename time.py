seconds = int(input("Enter a number: "))
minutes = 0
hours = 0
days = 0
if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
        if hours >= 24:
            days = hours // 24
            hours = hours % 24
list1 = [hours, minutes, seconds]
b = None
for i in list1:
    if i<10:
        b = f"{days} днів, {hours:02}:{minutes:02}:{seconds:02}"
    else:
        b = f"{days} днів, {hours}:{minutes}:{seconds}"
print(b)
from Project_1.student_import.Group import Group
from Project_1.student_import.student import Student
from Project_1.student_import.human import Human
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add(st1)
gr.add(st2)
print(gr)
assert gr.find('Jobs') == st1  # 'Steve Jobs'
assert gr.find('Jobs2') is None

gr.remove('Taylor')
print(gr) # Only one student

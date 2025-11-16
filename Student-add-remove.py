class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender} {self.age} {self.first_name} {self.last_name}"
students = {}
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        students[self.last_name] = self

    def info(self):
        return self.gender, self.age, self.first_name, self.last_name

    def __str__(self):
        return f"{self.gender} {self.age} {self.first_name} {self.last_name}"
class Group:

    def __init__(self, number):
        self.number = number
        self.amount = 0
        self.students = []
    def add(self, last_name):
        student = students.get(last_name)
        if not student:
            return None
        if student in self.students:
            return None
        self.students.append(student)
        self.amount += 1
    def remove(self, last_name):
        student1 = None
        for student in self.students:
            if student.last_name == last_name:
                student1 = student
                break
            else:
                continue
        if student1 == None:
            return None
        else:
            self.students.remove(student1)
            self.amount -= 1
    def find(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None
    def __str__(self):
        students = []
        for student in self.students:
            students.append(str(student))
        return f"The Group number: {self.number}, Amount of people: {self.amount} students: {students}"
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add("Jobs")
gr.add("Taylor")
print(gr)
assert str(gr.find('Jobs')) == str(st1), 'Test1'
assert gr.find('Jobs2') is None, 'Test2'
assert isinstance(gr.find('Jobs'), Student) is True

gr.remove('Taylor')
print(gr)  # Only one student

gr.remove('Taylor')  # No error!
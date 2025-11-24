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
    def add(self, person):
        if len(self.students) >= 3:
            # print("You can't add more than 10 students")
            return "you can't add more than 10 students."
        if person in self.students:
            return None
        self.students.append(person)
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
st3 = Student('Male', 30, 'Michael', 'Jordan', 'AN142')
st4 = Student('Male', 30, 'Oskar', 'Jackson', 'AN142')
gr = Group('PD1')
gr.add(st1)
gr.add(st2)
gr.add(st3)
gr.add(st4)
gr.add(st1)
gr.add(st2)
print(gr.find("Jobs"))
print(gr)
assert gr.find("Jobs") == st1

assert gr.find('Jobs2') is None

gr.remove('Taylor')
print(gr) # Only one student

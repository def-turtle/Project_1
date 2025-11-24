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
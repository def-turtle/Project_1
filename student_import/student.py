from human import Human
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
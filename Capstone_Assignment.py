# Design a Python program implementing multilevel inheritance (Person → Student → Exam) to compute and display total marks.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

class Exam(Student):
    def __init__(self, name, age, course, cs_marks, python_marks, math_marks):
        super().__init__(name, age, course)
        self.cs_marks = cs_marks
        self.python_marks = python_marks
        self.math_marks = math_marks
        self.t = self.python_marks + self.python_marks + self.math_marks

    def show(self):
        print(f"Name:- {self.name}")
        print(f"Age:- {self.age}")
        print(f"Course:- {self.course}")
        print(f"Cs_marks:- {self.python_marks}")
        print(f"Python_marks:- {self.python_marks}")
        print(f"Math_marks:- {self.math_marks}")
        print(f"Total Marks:- {self.t}")

student = Exam("Piyush", 18, "BCA", 97, 94, 98)
student.show()
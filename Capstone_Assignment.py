# Design a Python program implementing multilevel inheritance (Person → Student → Exam) to compute and display total marks.

class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.c = course

class Exam(Student):
    def __init__(self, name, age, course, marks1, marks2, marks3):
        super().__init__(name, age, course)
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3
        self.t = self.m1 + self.m2 + self.m3

    def show(self):
        print(f"Name:- {self.n}")
        print(f"Age:- {self.a}")
        print(f"Course:- {self.c}")
        print(f"Marks1:- {self.m1}")
        print(f"Marks2:- {self.m2}")
        print(f"Marks3:- {self.m3}")
        print(f"Total Marks:- {self.t}")

student = Exam("Piyush", 18, "BCA", 97, 94, 98)
student.show()
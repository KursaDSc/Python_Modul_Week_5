# Question2 - Kursad
import os

class School():

    def __init__(self,name,foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = []

    def add_new_student(self, student_name, class_name):
        self.students.append({"name":student_name,"class":class_name})

    def add_new_teacher(self, teacher_name, branch):
        self.teachers.append({"name":teacher_name,"branch":branch})

    def view_student_list(self):
        print(f"{'Name':<15} {'Class':<10}")
        print("-" * 25)
        for student in self.students:
            print(f"{student['name']:<15} {student['class']:<10}")
    
    def view_teacher_list(self):
        print(f"{'Name':<15} {'Major':<10}")
        print("-" * 25)
        for teacher in self.teachers:
            print(f"{teacher['name']:<15} {teacher['branch']:<10}")


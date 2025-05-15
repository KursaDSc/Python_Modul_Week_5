# Question2 - Furkan
class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = []

    def add_new_student(self, student_name, class_name):
        self.students.append((student_name, class_name))

    def add_new_teacher(self, teacher_name, branch):
        self.teachers.append((teacher_name, branch))

    def view_student_list(self):
        print("Ogrenci Listesi:")
        for student in self.students:
            print(f"Ad: {student[0]}, Sinif: {student[1]}")

    def view_teacher_list(self):
        print("Ogretmen Listesi:")
        for teacher in self.teachers:
            print(f"Ad: {teacher[0]}, Branş: {teacher[1]}")
#ornek liste
school = School("Istanbul Lisesi", 1950)
school.add_new_student("Ali Veli", "10A")
school.add_new_student("Ayşe Fatma", "11B")
school.add_new_teacher("Ahmet Hoca", "Matematik")
school.add_new_teacher("Zeynep Hoca", "Fizik")

school.view_student_list()
school.view_teacher_list()
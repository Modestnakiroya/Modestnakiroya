
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


class Lecturer(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}")


print("=== Student ===")
s = Student("modest", 22, "S123", "Computer Science")
s.display_info()

print("\n=== Lecturer ===")
l = Lecturer("Dr. arthur", 30, "Python")
l.display_info()

print("\n=== Staff ===")
st = Staff("Mr. Asasira", 38, "Administrator")
st.display_info()

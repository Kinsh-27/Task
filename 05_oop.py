''' Create a Student class with attributes for name, age,
 and grades. Include methods to display details and
 calculate the average grade.'''

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

student1 = Student("King", 20, [85, 95, 78, 82])
student1.display_details()
print(f"Average Grade: {student1.calculate_average_grade()}")

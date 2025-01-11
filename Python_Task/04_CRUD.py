''' Write a program that stores student data 
(name, age, grades) in a dictionary and performs CRUD operations.'''

students = {}
def create_student(student_id, name, age, grades):
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
    else:
        students[student_id] = {'name': name, 'age': age, 'grades': grades}
        print(f"Student {name} added successfully.")

def read_student(student_id):
    if student_id in students:
        print(f"Student ID: {student_id}")
        for key, value in students[student_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Student with ID {student_id} not found.")

def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = age
        if grades:
            students[student_id]['grades'] = grades
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student with ID {student_id} not found.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")


def CRUDE_Operations():
    while True:
        print("\n--- CRUDE_Operations ---")
        print("1. Create Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades = list(map(float, input("Enter Grades (separated by spaces): ").split()))
            create_student(student_id, name, age, grades)
        elif choice == '2':
            student_id = input("Enter Student ID to read: ")
            read_student(student_id)
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            age = input("Enter new Age (leave blank to keep unchanged): ")
            grades = input("Enter new Grades (leave blank to keep unchanged): ")
            update_student(student_id, name if name else None, int(age) if age else None, 
                           list(map(float, grades.split())) if grades else None)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            if students:
                print("\nAll Students:")
                for sid, data in students.items():
                    print(f"ID: {sid}, Name: {data['name']}, Age: {data['age']}, Grades: {data['grades']}")
            else:
                print("No student records found.")
        elif choice == '6':
            print("Exiting the Student")
            break
        else:
            print("Invalid choice. Please try again.")

CRUDE_Operations()

class Student:

    class_year= 2024
    num_students = 0 


    def __init__(self,name,age):
        self.name= name
        self.age = age
        Student.num_students += 1
student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)

print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")


print(f"{student1.name} is graduating in the year {Student.class_year}.")
print(f"{student2.name} is graduating in the year {Student.class_year}.")
print(f"Number of students: {Student.num_students}")

# -----------------------

print(f"{student1.name} is graduating in the year {Student.class_year}")
print(f"Number of students: {Student.num_students}")

# -----------------------

student3 = Student("Squidward" ,55)
student4 = Student("Sandy" , 27)

print(f"Student names: {student1.name}, {student2.name}, {student3.name}, {student4.name}")

Student.class_year = 2025

print(f"{student1.name} is graduating in the year {Student.class_year}.")
print(f"{student2.name} is graduating in the year {Student.class_year}.")
print(f"{student3.name} is graduating in the year {Student.class_year}.")
print(f"{student4.name} is graduating in the year {Student.class_year}.")
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average = average


class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average):
        super().__init__(name_of_vehicle, max_speed, average)

    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} passengers."


class A:
    def method_A(self):
        print("Method A from class A")

class B:
    def method_B(self):
        print("Method B from class B")

class C(A, B):
    def method_C(self):
        print("Method C from class C")

# Create an object of class C
obj = C()

# Access methods from class A and B using multiple inheritance
obj.method_A()
obj.method_B()
obj.method_C()




# Task 1: Create a Person class with properties, constructor, and methods

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def is_adult(self):
        return self.age >= 18


# Task 2: Implement Inheritance - Create a Student subclass

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Course: {self.course}"


# Task 3: Implement Polymorphism - Create a Teacher subclass

class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    def say_hello(self):  # Polymorphism - Override the say_hello method
        print(f"Hello, I am {self.name}, your {self.subject} teacher.")

    def get_teacher_info(self):
        return f"Teacher ID: {self.teacher_id}, Subject: {self.subject}"


# Testing the classes

# Create a Person
person = Person("Alice", 25, "Female")
person.say_hello()
print(f"Is {person.name} an adult? {person.is_adult()}")

# Create a Student
student = Student("Bob", 17, "Male", "S12345", "Math")
student.say_hello()
print(f"Is {student.name} an adult? {student.is_adult()}")
print(student.get_student_info())

# Create a Teacher
teacher = Teacher("Mr. Smith", 35, "Male", "T98765", "History")
teacher.say_hello()  # This calls the overridden method in Teacher
print(f"Is {teacher.name} an adult? {teacher.is_adult()}")
print(teacher.get_teacher_info())



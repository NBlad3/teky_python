from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id, gpa):
        super().__init__(name, age)
        self.student_id = student_id
        self.gpa = gpa  

    def get_student_id(self):
        return self.student_id
    
    def set_student_id(self, student_id: str):
        self.student_id = student_id

    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self, gpa: float):
        self.gpa = gpa

    def display_info(self):
        print(f"Student: {self.get_name()}, Age: {self.get_age()}")
        print(f"ID: {self.get_student_id()}, GPA: {self.get_gpa()}")
        print("-" * 40)


student1 = Student("John Doe", 20, "12345", 8.5)
student2 = Student("Emma Smith", 22, "67890", 4.5)

student1.display_info()
student2.display_info()

import datetime


class Student:
    
    def __init__(self, name, code, birth, gpa=0.0):
        if birth < int(datetime.datetime.now().strftime("%Y")) - 100 or birth > int(datetime.datetime.now().strftime("%Y")):
            raise Exception("Invalid birthdate")
        self.name = name
        self.birth = birth
        self.code = code
        self.gpa = gpa
    
    def update_score(self, new_gpa):
        self.gpa = new_gpa
    
    def check_academic_performance(self):
        if self.gpa >= 8.0:
            print("Academic Performance: Excellent")
        elif self.gpa >= 6.5:
            print("Academic Performance: Good")
        elif self.gpa >= 5.0:
            print("Academic Performance: Average")
        else:
            print("Academic Performance: Poor")
    
    def __str__(self):
        return f"Name: {self.name}\nCode: {self.code}\nBirthdate: {self.birth}\nAverage Score: {self.gpa}"


s1 = Student("Nguyen", 123, 2000)
s1.update_score(5.5)
s1.check_academic_performance()
print(s1)
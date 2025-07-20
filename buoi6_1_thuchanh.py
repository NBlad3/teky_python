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
        return f"Name: {self.name}\nCode: {self.code}\nBirthdate: {self.birth}\nAverage Score: {self.gpa}\n"


s1 = Student("Nguyen", 123, 2000)
s1.update_score(5.5)
s1.check_academic_performance()
print(s1)

s2 = Student("Tran", 456, 1999)
s2.update_score(8.0)
s2.check_academic_performance()
print(s2)

s3 = Student("Le", 789, 2001)
s3.update_score(6.5)
s3.check_academic_performance()
print(s3)

s4 = Student("Pham", 101, 2002)
s4.update_score(4.0)
s4.check_academic_performance()
print(s4)

s5 = Student("Duy", 101, 2003)
s5.update_score(5.0)
s5.check_academic_performance()
print(s5)

s6 = Student("Duc", 101, 2004)
s6.update_score(4.0)
s6.check_academic_performance()
print(s6)
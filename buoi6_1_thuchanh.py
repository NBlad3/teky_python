import datetime

class Student:
    def __init__(self, last, birth, code):
        if birth < int(datetime.datetime.now().strftime("%Y")) - 100 or birth > int(datetime.datetime.now().strftime("%Y")):
            raise Exception("Invalid birthdate")
        self.last = last
        self.birth = birth
        self.code = code
    def __str__(self):
        return f"Last Name: {self.last}\nBirthdate: {self.birth}\nStudent code: {self.code}\n"
    
s1 = Student("Pham", 2000, 123)
s2 = Student("Nguyen", 2000, 321)

print(s1)
print(s2)
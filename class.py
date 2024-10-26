import random

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def get_perimeter(self):
        if self.validate():
            return self.a + self.b + self.c
        else:
            return None
    
    def get_area(self):
        if self.validate():
            p = self.get_perimeter() / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return None
    
    def get_info(self):
        perimeter = self.get_perimeter()
        area = self.get_area()
        return f"a: {self.a}, b: {self.b}, c: {self.c} - perimeter: {perimeter}, area: {area}\n"

if __name__ == "__main__":
    with open("triangle2.txt", "w") as file:
        for i in range(100):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100) 
            triangle = Triangle(a, b, c)
            file.write(triangle.get_info())





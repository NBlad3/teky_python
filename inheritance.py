
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def makeSound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def makeSound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, age, furColor):
        super().__init__(name, age)

        self.furColor = furColor

    def makeSound(self):
        print("Meow!")

dog = Dog("Steve", 3, "Brown")
cat = Cat("Alex", 2, "Gray")

dog.makeSound()  
cat.makeSound()





class Book:
    def __init__(self, title, author, year, available=True):
        self._title = title
        self._author = author
        self._year = year
        self._available = available

    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_year(self):
        return self._year
    def is_available(self):
        return self._available

    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    def set_year(self, year):
        self._year = year
    def set_availability(self, available):
        self._available = available
 

    def display_info(self):
        availability = "Available" if self._available else "Not available"
        print(f"Title: {self._title}\nAuthor: {self._author}\nYear: {self._year}\nStatus: {availability}")
 
 

book1 = Book("Moby-Dick", "Herman Melville", 1851)
 

book1.set_availability(False)
 

book1.display_info()
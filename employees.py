from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getBirthDate(self):
        pass

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def setType(self, type):
        pass

    @abstractmethod
    def reward(self):
        pass

class FinanceEmployee(Employee):
    def __init__(self, id, name, birth_date, type):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.type = type

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getBirthDate(self):
        return self.birth_date

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def reward(self):
        if self.type == "Excellent" or self.type == "Good":
            return True
        else:
            return False

class ContractEmployee(Employee):
    def __init__(self, id, name, birth_date, type):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.type = type

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getBirthDate(self):
        return self.birth_date

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def reward(self):
        if self.type == "Excellent" or self.type == "Good":
            return True
        else:
            return False
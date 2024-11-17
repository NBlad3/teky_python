from abc import ABC

class Student(ABC):
    def getStudentName(self):
        return self.name

    def getStudentAddress(self):
        return self.address

    def getStudentID(self):
        return self.id

    def calculateGPA(self):
        self.gpa = sum(self.scores) * 3 / 6
        if self.address != "Hanoi":
            self.gpa += 0.5
        return self.gpa

class GoodStudent(Student):
    def __init__(self, id, name, address, scores):
        self.id = id
        self.name = name
        self.address = address
        self.scores = scores
        self.gpa = self.calculateGPA()

class PassStudent(Student):
    def __init__(self, id, name, address, scores):
        self.id = id
        self.name = name
        self.address = address
        self.scores = scores
        self.gpa = self.calculateGPA()

class FailStudent(Student):
    def __init__(self, id, name, address, scores):
        self.id = id
        self.name = name
        self.address = address
        self.scores = scores
        self.gpa = self.calculateGPA()

def main():
    students = []

    student_data = {}
    with open('students.txt', 'r') as students_file:
        next(students_file)
        for line in students_file:
            parts = line.strip().split(',')
            student_id = parts[0].strip()
            student_name = parts[1].strip()
            student_address = parts[2].strip()
            student_data[student_id] = (student_name, student_address)

    exam_results = {}
    with open('exam_results.txt', 'r') as results_file:
        next(results_file)
        for line in results_file:
            parts = line.strip().split(',')
            student_id = parts[0].strip()
            grades = []
            for grade in parts[1:]:
                grades.append(float(grade.strip()))
            exam_results[student_id] = grades

    for student_id, scores in exam_results.items():
        if student_id in student_data:
            name, address = student_data[student_id]
            gpa = sum(scores) * 3 / 6
            if address != "Hanoi":
                gpa += 0.5

            if gpa >= 8:
                student = GoodStudent(student_id, name, address, scores)
                students.append(student)
            elif gpa >= 5:
                student = PassStudent(student_id, name, address, scores)
                students.append(student)
            else:
                student = FailStudent(student_id, name, address, scores)
                students.append(student)

    excellent_students = [student.getStudentName() for student in students if isinstance(student, GoodStudent)]
    failing_students = [student.getStudentName() for student in students if isinstance(student, FailStudent)]

    if excellent_students:
        print(f"Congrats {', '.join(excellent_students)} on passing the course with excellent grades.")
    if failing_students:
        print(f"{', '.join(failing_students)} need to do better next time!")

if __name__ == "__main__":
    main()

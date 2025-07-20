"""
Create the parent class Employee:
It has a __init__ method with the following attributes: full_name, employee_id, base_salary.
It has a display_information() method to print basic information.
Have a method tinh_luong_thang() that temporarily returns self.luong_co_ban.
Create a child class QuanLy(NhanVien):
Inherit from NhanVien.
In __init__, receive an additional parameter phu_cap_chuc_vu.
Use super().__init__(...) to call the constructor of NhanVien.
Add the attribute self.phu_cap_chuc_vu.
Override the method tinh_luong_thang(): The monthly salary of a manager is equal to luong_co_ban + phu_cap_chuc_vu.
Create a subclass LapTrinhVien(NhanVien):
Inherit from NhanVien.
In __init__, add the parameter so_gio_lam_them.
Use super().__init__(...).
Add the attribute self.so_gio_lam_them.
Override the monthly_salary() method: The monthly salary of a programmer will be equal to base_salary + (overtime_hours * 200000). (Assuming 200k/hour).
Testing:
Create an object manager_A from the Manager class.
Create an object named programmer_B from the Programmer class.
Call the display_information() and calculate_monthly_salary() methods on both objects and print the results to see the difference.
Use isinstance() to check if manager_A is an Employee.
Commit the code to GitHub.
"""

class Employee():
    def __init__(self, full_name, employee_id, base_salary):
        self.full_name = full_name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def display_information(self):
        print(f'Full name: {self.full_name}')
        print(f'Employee ID: {self.employee_id}')
        print(f'Base salary: {self.base_salary}')

    def calculate_monthly_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, full_name, employee_id, base_salary, extra_salary):
        super().__init__(full_name, employee_id, base_salary)
        self.extra_salary = extra_salary

    def calculate_monthly_salary(self):
        return self.base_salary + self.extra_salary

class Programmer(Employee):
    def __init__(self, full_name, employee_id, base_salary, overtime_hours):
        super().__init__(full_name, employee_id, base_salary)
        self.overtime_hours = overtime_hours

    def calculate_monthly_salary(self):
        return self.base_salary + (self.overtime_hours * 200000)


manager = Manager('Nguyen Van A', 1, 50000000, 10000000)
programmer = Programmer('Nguyen Van B', 2, 50000000, 50)

print(manager.display_information())
print(manager.calculate_monthly_salary())
print("-" * 40)
print(programmer.display_information())
print(programmer.calculate_monthly_salary())
print("-" * 40)
print(isinstance(manager, Employee))
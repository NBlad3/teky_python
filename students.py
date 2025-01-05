n = int(input("So luong hoc sinh: "))
student_list = []

for i in range(n):
    name = input("Ten: ")
    while len(name) < 2:
        name = input("Ten: ")
    
    math = float(input("Diem toan: "))
    while math < 0 or math > 10:
        math = float(input("Diem toan: "))
    
    english = float(input("Diem anh: "))
    while english < 0 or english > 10:
        english = float(input("Diem anh: "))
    
    write = float(input("Diem van: "))
    while write < 0 or write > 10:
        write = float(input("Diem van: "))

    print("\n")
    student_list.append([name, math, english, write])

print("\n")

def calculate_grade(average):
    if average < 5:
        return "Yeu"
    elif average < 6.5:
        return "Trung binh"
    elif average < 8:
        return "Kha"
    else:
        return "Gioi"

def display_student_info(student):
    average = round((student[1] + student[2] + student[3]) / 3, 2)
    print(f"Ten: {student[0]}")
    print(f"Diem trung binh: {average}")
    print(calculate_grade(average))
    print("\n")

for student in student_list:
    display_student_info(student)

while True:
    print("1. Them hoc sinh\n2. Xoa hoc sinh\n3. Sua thong tin hoc sinh\n4. Hien thi danh sach hoc sinh\n5. Thoat\n")
    
    choice = int(input("Lua chon: "))
    
    if choice == 1:
        name = input("Ten: ")
        while len(name) < 2:
            name = input("Ten: ")
    
        math = float(input("Diem toan: "))
        while math < 0 or math > 10:
            math = float(input("Diem toan: "))
    
        english = float(input("Diem anh: "))
        while english < 0 or english > 10:
            english = float(input("Diem anh: "))
    
        write = float(input("Diem van: "))
        while write < 0 or write > 10:
            write = float(input("Diem van: "))

        print("\n")
    
        student_list.append([name, math, english, write])

    elif choice == 2:
        delete_name = input("Xoa: ")
        for student in student_list:
            if student[0] == delete_name:
                student_list.remove(student)
                break
        print("\n")    

    elif choice == 3:
        change_name = input("Doi: ")
        for student in student_list:
            if student[0] == change_name:
                student[1] = float(input("Diem toan: "))
                student[2] = float(input("Diem anh: "))
                student[3] = float(input("Diem van: "))
                break
        print("\n")

    elif choice == 4:
        for student in student_list:
            display_student_info(student)

    elif choice == 5:
        break
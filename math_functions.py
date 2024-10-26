def divide_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

def devide_2():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)

def isPrime():
    n = int(input("Nhap so: "))
    flag = True

    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

    if flag:
        print("Prime")
    else:
        print("Not Prime")

#divide_3()

#devide_2()

isPrime()
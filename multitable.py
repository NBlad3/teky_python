with open("multitable.txt", "w") as f:
    for x in range(2, 10):
        for y in range(1, 11):
            f.write(f"{x} * {y} = {x * y}\n")
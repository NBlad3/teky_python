import random
import math

def generate_random_triangles(num_triangles=100):
    triangles = []
    for _ in range(num_triangles):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        triangles.append((a, b, c))
    return triangles

def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_perimeter(a, b, c):
    return a + b + c

def calculate_area(a, b, c):
    s = calculate_perimeter(a, b, c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    triangles = generate_random_triangles()

    with open('triangle1.txt', 'w') as f:
        for triangle in triangles:
            f.write(' '.join(map(str, triangle)) + '\n')

    triangle_results = {}
    for a, b, c in triangles:
        if is_triangle(a, b, c):
            perimeter = calculate_perimeter(a, b, c)
            area = calculate_area(a, b, c)
            triangle_results[(a, b, c)] = (True, perimeter, area)
        else:
            triangle_results[(a, b, c)] = False

    with open('triangle_validation.txt', 'w') as f:
        for key, value in triangle_results.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()

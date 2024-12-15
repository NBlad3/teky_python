def analyze_numbers(*numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    if len(even_numbers) > len(odd_numbers):
        return "There are more even numbers than odd numbers."
    elif len(even_numbers) < len(odd_numbers):
        return "There are more odd numbers than even numbers."
    else:
        return "There are an equal number of even and odd numbers."

result = analyze_numbers(1, 2)
print(result)

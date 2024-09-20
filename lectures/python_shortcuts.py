# syntax for list comprehension is
    # expression for identifier in sequence

total = sum(k * k for k in range(1, 11))
print(total)

numbers = list(range(1, 11))
squares = [i*i for i in numbers]
cubes = [1, 8, 27, 64, 125]
powers = list(zip(numbers, squares, cubes))
print(powers)
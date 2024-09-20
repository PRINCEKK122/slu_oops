import math

# Miles to Kilometers
miles = float(input("Enter a distance in miles: "))
kilometers = round(miles * (8 / 5), 2)
print("Converting " + str(miles) + " to kilometers and rounding it to 2 d.p is: " + str(kilometers))
print('*' * 100)

# # Square Root Approximation using the Babyloanian method
value = int(input("Enter a number: "))
guess = value / 2

next_guess = guess + (value / guess) / 2
second_next_guess = round((next_guess + (value / next_guess)) / 2, 2)


print("Square root of the number " + str(value) + " is to 2 decimal places: " + str(second_next_guess))
print('*' * 100)
# Quadratic Equation Solver
question = "Enter the coefficient of "
a_coefficient = int(input(question + " a: "))
b_coefficient = int(input(question + " b: "))
c_coefficient = int(input(question + " c: "))

square_root = math.sqrt(pow(b_coefficient, 2) - (4 * a_coefficient * c_coefficient))

first_root = round((-b_coefficient + square_root) / 2 * a_coefficient, 2)
second_root = round((-b_coefficient - square_root) / 2 * a_coefficient, 2)

print("The roots are " + str(first_root) + " and " + str(second_root))
print('*' * 100)

# Even or odd
number = int(input("Enter an integer: ")) % 2
result = "Even" * (number == 0) + "Odd" * (number != 0)
print(result)

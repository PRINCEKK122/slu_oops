##########################
## Question 1
##########################
number = int(input("Enter a positive number: "))
is_prime = True

if number == 1:
    is_prime = False
else:
    for i in range(2, 1 + int(number**(1/2))):
        if (number % i == 0):
            is_prime = False

print(f"The number {number} is {'not' * (not is_prime)} prime.")


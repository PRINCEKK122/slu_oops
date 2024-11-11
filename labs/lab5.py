def add(a, b):
    for _ in range(b):
        a += 1

    return a

def multiply(a, b):
    x = 0
    for _ in range(b):
        x = add(x, a)
    return x

def power(a, b):
    x = 1
    for _ in range(b):
        x = multiply(x, a)
    
    return x


if __name__ == "__main__":
    from random import randint

    user_input = int(input("Enter any positive integer: "))
    exponent = randint(1, 5)
    result = power(user_input, exponent)

    print(f"Your input was {user_input} and {user_input} to the power of {exponent} is {result}")




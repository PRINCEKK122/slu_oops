from random import randint

for _ in range(3):
    numbers = []
    for _ in range(100):
        numbers.append(randint(1, 1000))

    for i, num in enumerate(numbers):
        if i % 10 == 0:
            print()
        print(f"{num:>5}", end = "")
        
    print()
    print()
    print(f"High: {max(numbers)}, Low: {min(numbers)}, Average: {sum(numbers) / len(numbers)}")

# CSCI 5010
# Machine Problem 2
#
# Prince Awuah Karikari
#
# Description: This script prints random 100 integers
# from the range of 1 to 1000 and prints them in a
# 10 x 10 grid.

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

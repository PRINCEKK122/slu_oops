########################
### Slicing
########################
user_input = input("Enter a sentence? ")
# Extracting characters 4 to 9
print(user_input[4:10])

# Reversing the string using slice
print(user_input[::-1])

# Enusre theat the sentence contains 3 words
words = user_input.split()
words[0], words[-1] = words[-1], words[0]


# Modified sentence after swapping
modified_sentence = " ".join(words)

print(modified_sentence)


###########################
#### For Loops
###########################
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for i, fruit in enumerate(fruits):
    index = len(fruits) - i - 1
    print(index, fruits[index])

# Use range to print all even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i)

# Task 3
numbers = [2, 2.5, 3, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print("Modified list", numbers)

sorted()

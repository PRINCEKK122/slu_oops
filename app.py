import array

# 9th September, 2024
# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(number)

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in myList:
#     print(number)

# sum = 0
# for number in myList:
#     sum += number

# print(sum)

# name = 'Karikari'
# for letter in name:
#     print(letter)

# groceries = ["milk", "eggs", "bread", "ham"]
# count = 0
# for item in groceries:
#     count += 1
#     print(str(count) + ". " + item)

# for k, item in enumerate(groceries):
#     print(str(k + 1) + ". " + item)

# for i, letter in enumerate(name):
#     print("Index " + str(i) + ": " + letter)

# guests = ["Carol", "Alice", "Bob"]
# for person in guests:
#     person = person.lower()

# for i, person in enumerate(guests):
#     guests[i] = person.lower()

# print(guests)

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

uppers = tuple(uppercase)
lowers = tuple(lowercase)

for i in range(11):
    for j in range(11):
        print(i + j, end = "\t")
    print()

for i in range(len(uppers)):
    print(str(i + 1) + " " + lowers[i] + " " + uppers[i])

prime_numbers = []
for number in range(2, 100):
    is_prime = True
    for num in range(2, number):
        if (number % num == 0):
            is_prime = False
            break

    if (is_prime):
        prime_numbers.append(number)

print(prime_numbers)
   
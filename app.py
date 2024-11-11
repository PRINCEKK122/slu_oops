# person = "Usain Bolt"
# distance = 100
# time = 9.5852569

# print(f"{person} ran {distance} meters in {time:1.2f} seconds.")
# myFile = None
# while not myFile:
#     fileName = input('What is the filename: ')
#     try:
#         myFile = open(fileName)
#         print(myFile.readlines())
#         myFile.close()
#     except OSError:
#         print(f'Sorry. Unable to open file {fileName}')

# filename = input("What is the filename? ")
# with open(filename, 'x') as source:
#     text = source.read()
#     numchars = len(text)
#     numwords = len(text.split())
#     numlines = len(text.split('\n'))

# print(numlines, numwords, numchars)

# print("Mon", "Tue", "Wed", "Thu", "Fri", sep="-", end=":")

# print("My teacher", teacherName, "gave me a", testScore, "on the test.")
# print("My total class grade is now", str(totalAverage + "."))
# fileName = open("resume.txt")

# for line in fileName:
#     print(line.rstrip())

# fileName.close()


# primes = {2, 3, 5, 7}
# evens = {2, 4, 6, 8}
# primes.add(11)
# print(primes)
# evens.discard(8)
# print("Evens", evens)

# print(primes ^ (evens))

# person = {"name": "Prince", "age": 32}
# person["name"][0] = "z"
# print({i * i * i: i for i in range(1, 101)})

# with open("loremipsum.txt") as source:
#     numlines = numwords = numchars = 0
#     line = source.readline()

#     while line:
#         numchars += len(line)
#         numwords += len(line.split())
#         numlines += 1

#         # done with the current line, read the next line
#         line = source.readline()

# print(numlines, numwords, numchars)


class Student:
    def __init__(self, name):
        self._name = name
        self._testScores = []

    def testAvg(self):
        if len(self._testScores) == 0:
            return None
        return sum(self._testScores) / len(self._testScores)

    def addTest(self, score):
        self._testScores.append(score)

    def __str__(self):
        return f"{self._name} {self._testScores}"


# roster = []

# name = input("Enter your name: ")
# while name:
#     student = Student(name)
#     testScores = input("Enter your scores: ")

#     for num in testScores.split():
#         student.addTest(int(num))
#     roster.append(student)
#     name = input("Enter your name: ")

# for student in roster:
#     print(student)


def print_rangoli(size):
    # alphabets = [chr(i) for i in range(97, 123)]
    # indices = [i for i in range(size)]
    # combined = indices + indices[:-1][::-1]
    # idx = 0

    # for i in range(size):
    #     combined[idx] = alphabets[i]
    #     idx += 1

    # for i in range(size - 2, -1, -1):
    #     combined[idx] = alphabets[i]
    #     idx += 1

    # print("-".join(combined))
    alphabets = [chr(i) for i in range(97, 123)]
    alphabets = alphabets[:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]

    for i in indices:
        start_idx = i + 1
        original = alphabets[-start_idx:]
        reverse = original[::-1]
        row = reverse + original[1:]
        width = 4 * size - 3
        print("-".join(row).center(width, "-"))


def doSomething(x, y):
    x = [2, 3]
    y[0] = 1

x = [1, -1]
y = [2, 4]
doSomething(x, y)
print(">>>>", x[0], x[1], y[0])

def reverseOrder(nums):
    if len(nums) > 0:
        print(nums[-1], end=" ")
        nums.pop()
        reverseOrder(nums)


reverseOrder([1, 2, 3, 4, 5])

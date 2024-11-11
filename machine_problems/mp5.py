from student import Student


def getStudents():
    #
    # Opens the data file of student info... studentID, firstName, lastName, then
    # testScores - the number of test scores is variable, from zero up... reads
    # each line of data as a str, divides the line into the values... str, str, str,
    # int, int, int... (a variable number of int values - could be none)...
    # instantiates a new Student object, uses the Student object's instance methods
    # to add those values to the object, adds the Student object to a dict of objects,
    # and returns the dict of Student objects.
    #
    # There are no parameters.
    #
    # Returns a dict of objects from the Student class
    #
    students_dict = {}

    with open("5010 - MP5 Data.txt") as source:
        for line in source:
            data = line.rstrip().split()

            id = data[0]
            student = Student(id)

            firstName = data[1]
            lastName = data[2]
            student.setName(firstName, lastName)

            testScores = data[3:]
            for score in testScores:
                student.addTest(int(score))

            students_dict[id] = student

    return students_dict


def updateName(roster, stuID):
    #
    # Prompts the user to enter the first name and last name of a student. Then,
    # uses the setName() instance method to change the name for the Student object
    # in the dictionary roster with the key = stuID.
    #
    # roster A dictionary of objects from the Student class, using stuID as the
    # key, and a Student object as the value.
    # stuID A str that is the key for a Student object in the dictionary roster.
    #
    # There is no return value.
    #
    student = roster[stuID]
    student.setName(input("Enter first name: "), input("Enter last name: "))
    print(f"\n{student}")


def updateTests(roster, stuID):
    #
    # Prompts the user to enter test scores for a student using addTest() to add
    # each one to the Student object in the dictionary roster with the key = stuID.
    #
    # roster A dictionary of objects from the Student class, using stuID as the
    # key, and a Student object as the value.
    # stuID A str that is the key for a Student object in the dictionary roster.
    #
    # There is no return value.
    #
    user_prompt = "Enter a Test Score (<enter> to stop): "
    testScore = input(user_prompt)

    student = roster[stuID]
    while testScore:
        student.addTest(int(testScore))
        testScore = input(user_prompt)


if __name__ == "__main__":
    roster = getStudents()

    for student in roster.values():
        print(student)

    print("You may update any student info, or add a student.\n")
    idPrompt = "Enter Student ID (<enter to stop>): "
    userInput = input(idPrompt)

    while userInput:
        if userInput not in roster:
            print("This student does not exist. You may enter the info now.")

            student = Student(userInput)
            student.setName(input("First Name: "), input("Last Name: "))
            roster[student.getID()] = student
            updateTests(roster, student.getID())

            print("\nNew Student Added:")
            print(student)

            userInput = input(f"{idPrompt}")
        else:
            student = roster[userInput]
            print(student)

            print("(1) Change the Name")
            print("(2) Add a Test\n")

            userChoice = input("What would you like to do? (<enter> to stop): ")
            if userChoice == "1":
                updateName(roster, student.getID())
            elif userChoice == "2":
                updateTests(roster, student.getID())
                print(f"\n{student}")
            else:
                print()

            userInput = input(f"{idPrompt}")

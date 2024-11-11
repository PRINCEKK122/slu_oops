
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

    students = {}
    sourceFile = open("5010 - MP5 Data.txt")
    
    for line in sourceFile:
        data = line.rstrip().split()

        student = Student(data.pop(0))
        student.setName(data.pop(0), data.pop(0))

        scores = [int(score) for score in data]
        for score in scores:
            student.addTest(score)

        students[student.getID()] = student
    sourceFile.close()
    
    return students

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
    student = roster[stuID]
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    student.setName(fName, lName)
    
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
    score = input("Enter a Test Score (<enter> to stop): ")

    student = roster[stuID]
    while score:
        student.addTest(int(score))
        score = input("Enter a Test Score (<enter> to stop): ")


if __name__ == "__main__":
    roster = getStudents()

    for student in roster:
        print(roster[student])

    print("You may update any student info, or add a student.\n")
    userInput = input("Enter Student ID (<enter to stop>): ")

    while userInput:
        if userInput not in roster:
            print("This student does not exist. You may enter the info now.")

            student = Student(userInput)
            student.setName(input("First Name: "), input("Last Name: "))
            roster[student.getID()] = student
            updateTests(roster, student.getID())

            print()
            print("New Student Added:")
            print(student)

            userInput = input("Enter Student ID (<enter to stop>): ")
        else:
            student = roster[userInput]
            print(student)

            print("(1) Change the Name")
            print("(2) Add a Test")
            print()

            option = input("What would you like to do? (<enter> to stop): ")
            if option == "1":
                updateName(roster, student.getID())
            elif option == "2":
                updateTests(roster, student.getID())
                print(f"\n{student}")
            else:
                print()
            
            userInput = input("Enter Student ID (<enter to stop>): ")

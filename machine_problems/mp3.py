#
# Machine Problem 3
# Prince Awuah Karikari
#
# Description: This script provides math practice problems. The user is given 
#              2 integers to add, subtract, or multiply. The user gives an
#              answer and is told if they are correct, or not. The user is
#              given another problem and can continue by entering 'y' or 'yes'.
#              The number of correct and the number of incorrect answers are 
#              recorded after each problem

from random import *

def mathProblem(problemNum):

    #
    # Prompts the user with a math problem (+, -, or *) with 2 random int
    # values between 0 and 20. Collect the answer from the user, and 
    # generates the correct answer.
    #
    # problemNum    An int value.
    #
    # Returns a tuple with 2 elements. The 1st element is the user's
    # answer(int) and the 2nd element is the correct answer(int)
    
    num1, num2 = sample(range(0, 20), 2)

    operator = choice(("+", "-", "*"))
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    
    print(f"Problem {problemNum}: {num1} {operator} {num2} = ", end = "")
    return (int(input()), answer)

def gradeAnswer(answers, answerTally):

    #
    # Checks to see if the user's answer and the correct answer are the same.
    # Prints the appropriate message to the user, along with a running total
    # of how many right and wrong answers the user's has accumlated in this 
    # session.
    # 
    # answers       A tuple with 2 elements. The 1st element is the user's
    #               answer (int) and the 2nd element is the correct answer (int).
    # answerTally   a list with 2 elements. The 1st element is a running total
    #               of how many right answers so far in this session (int),
    #               and the 2nd element is a running total of how many wrong
    #               answers so far in this session (int). The list is modified
    #               in the function.

    # There is no return value

    if answers[0] == answers[1]:
        answerTally[0] += 1
        print("You are right!")
    else:
        answerTally[1] += 1
        print(f"Sorry, that is not correct. The correct answer is {answers[1]}")

    print()
    print(f"So far... {answerTally[0]} right, {answerTally[1]} wrong.")
    print()

### Main Program ###
print()
print("MATH PRACTICE PROBLEMS")
print()

print("Add, Subtract, or Multiply the numbers together.")
print("I'll tell you if you are right or wrong.")
print()

problemNum = 1
tally = [0, 0]
gradeAnswer(mathProblem(problemNum), tally)

prompt = "Do you want to perform another problem? ('Y' or 'N') "
userPrompt = input(prompt).lower()
print()

while not(userPrompt in ("n", "no")):
    problemNum += 1
    gradeAnswer(mathProblem(problemNum), tally)
    userPrompt = input(prompt).lower()
    print()

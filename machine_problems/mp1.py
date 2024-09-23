
# CSCI 5010
# Machine Problem 1
#
# Prince Awuah Karikari
#
# Description: This script prompts the user for their name, job, annual salary,
# and monthly rent. A greeting is printed, along with the name
# the job. The annual salary, monthly salary, take home pay, and
# monthly spending money calculation are displayed. The
# calculations require only 1 assumption - that take home pay
# will be 65% of the gross salary.
#

print("Let's see how much spending money you will have when you graduate.")
print()

name = input("What is your name? ")
occupation = input("What job will you have? ")
annual_salary = float(input("What will be your annual salary? "))
monthly_rent = int(input("What will be your monthly rent? "))
print()

monthly_salary = annual_salary / 12
net_salary = monthly_salary * 0.65
remaining_funds_after_rent = net_salary - monthly_rent

print("Hello " + name + ", " + occupation + ".")
print("Your annual salary of " + str(annual_salary) + " means $" + str(monthly_salary) + " per month.")
print("Take home pay will be $" + str(net_salary) + " per month.")
print("After rent is paid, you will have $" + str(remaining_funds_after_rent) + " per month to spend.")

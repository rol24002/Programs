"""
Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60
Ask the user for their grade percentage, then write a series of if-elif-else statements 
to print out the appropriate letter grade. (At this point, you'll have a separate print 
statement for each grade letter in the appropriate block.)

Assume that you must have at least a 70 to pass the class. After determining the letter 
grade and printing it out. Add a separate if statement to determine if the user passed the course, 
and if so display a message to congratulate them. If not, display a different message to encourage 
them for next time.

Change your code from the first part, so that instead of printing the letter grade in the body of each if,
elif, or else block, instead create a new variable called letter and then in each block, set this variable
to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print
statement that prints the letter grade once.
"""
print("Grade Calculator")
num = float(input("Enter Grade Percent:"))
#if statement numbet
if num >= 90:
    grade = "A"
elif num >= 80:
    grade = "B"
elif num >= 70:
    grade = "C"
elif num >= 60:
    grade = "D"
else:
    grade = "F"
#if sign
    sign=""
last_digit = grade % 10
if last_digit >= 7:
    sign="+"
elif last_digit < 3:
    sign = "-"
else:
    sign=""
print()
print(f"Your Grade Letter is: {grade.capitalize()}{sign}")
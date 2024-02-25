# Write a program that prints a message if a variable is less than or equal to
# 10, another message if the variable is greater than 10 but less than or equal
# to 25, and another message if the variable is greater than 25.

variable = int(input("Enter a number: "))
if variable <= 10:
    print("Hello!")
if 10 > variable <= 25:
    print("Hey!")
if variable > 25:
    print("Great!")
# 6. Write a program with a variable age assigned to an integer that prints different strings depending on what integer age is.

age = int(input("Enter an age: "))
if age < 18:
    print("You are Underaged.")
if age >= 18:
    print("You are an adult.")
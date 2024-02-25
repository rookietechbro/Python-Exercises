from math import sqrt

def divide_or_square(number: float) -> float:
    if number % 5 == 0:
        return sqrt(number)

    elif number % 5 != 0:
        return number % 5

number = float(input("Enter a number: "))

#put in your function next.

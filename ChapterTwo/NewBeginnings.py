print("Enter two integers and I will tell you the \
relationships they satisfy.")
number1 = int(input("Enter a first integer: "))
number2 = int(input("Enter a second integer: "))

if number1 == number2:
    print(number1, "is equal to", number2)
if number1 != number2:
    print(number1, "is not equal to",  number2)
if number1 < number2:
    print(number1, "is less than", number2)
if number1 > number2:
    print(number1, "is greater than", number2)
if number1 <= number2:
    print(number1,"is less than or equals to", number2)
if number1 >= number2:
    print(number1,"is greater than or equals to", number2, "\n")




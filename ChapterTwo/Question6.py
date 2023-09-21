#(Odd or Even) Use if statements to determine whether an integer is
#odd or even. [Hint: Use the remainder operator. An even number is a
#multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by
#2.]

print("Enter a number and I will determine if it is odd or even.")
number = int(input("Number: "))
if number % 2 == 0:
    print("This is an even number")
if number % 2 == 1:
    print("This is an odd number")


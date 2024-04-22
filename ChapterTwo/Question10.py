# (Arithmetic, Smallest and Largest) Write a script that inputs three
# integers from the user. Display the sum, average, product, smallest and
# largest of the numbers. Note that each of these is a reduction in functional style
# programming.

integer1 = int(input("Enter a first number: "))
integer2 = int(input("Enter a second number: "))
integer3 = int(input("Enter a third number: "))

print("The sum is", integer1 + integer2 + integer3, '.')
print("The largest number is", max(integer1, integer2, integer3), '.')
print("The smallest number is", min(integer1, integer2, integer3), '.')

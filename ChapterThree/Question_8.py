# 3.8 (Arithmetic, Smallest and Largest)
# In Exercise 2.10, you wrote a script that input three integers,
# then displayed the sum, average, product, smallest and largest of those values.
# Reimplement your script with a loop that inputs four integers.


counter = 0
total = 0
product = 1
minimum = 0
maximum = 0
number = int(input("Enter a number, however, to end collection, enter 0: "))

while number != 0:
    counter += 1
    total += number
    product *= number
    number = int(input("Enter a number, however, to end collection, enter 0: "))

    if counter != 0:
        Average = total / counter

    if minimum < number:
         minimum = number
    # else:
    #     number = minimum
    #
    # if maximum > number:
    #     number = maximum

print('The total is', total)
print(f'The average of the numbers is {(total / counter): .2f}')
print(f'Tne product of the numbers is {product}')
print(f'The minimum is {minimum}')
# print(f'The maximum is {maximum}')

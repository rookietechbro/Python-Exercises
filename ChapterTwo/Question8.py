#(Table of Squares and Cubes) Write a script that calculates the squares
#and cubes of the numbers from 0 to 5. Print the resulting values in table
#format, as shown below. Use the tab escape sequence to achieve the threecolumn
#output.

numbers = int(input(5))
square_of_numbers = numbers * numbers
cube_of_numbers = numbers * numbers * numbers
print(numbers, square_of_numbers, cube_of_numbers)

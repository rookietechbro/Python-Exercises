#(Table of Squares and Cubes) Write a script that calculates the squares
#and cubes of the numbers from 0 to 5. Print the resulting values in table
#format, as shown below. Use the tab escape sequence to achieve the threecolumn
#output.

print('Numbers\t\t Squares\t\t Cubes\t\t')

number0 = 0
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5

square0 = number0 * number0
square1 = number1 * number1
square2 = number2 * number2
square3 = number3 * number3
square4 = number4 * number4
square5 = number5 * number5

cube0 = square0 * number0
cube1 = square1 * number1
cube2 = square2 * number2
cube3 = square3 * number3
cube4 = square4 * number4
cube5 = square5 * number5

print(number0, '\t\t\t' ,square0, '\t\t\t\t', cube0)
print(number1, '\t\t\t' ,square1, '\t\t\t\t', cube1)
print(number2, '\t\t\t' ,square2, '\t\t\t\t', cube2)
print(number3, '\t\t\t' ,square3, '\t\t\t\t', cube3)
print(number4, '\t\t\t' ,square4, '\t\t\t', cube4)
print(number1, '\t\t\t' ,square5, '\t\t\t', cube5)

#Lines 37 t0 43 shows right alignation. please uncomment to view...
#print('Numbers\t\t Squares\t\t Cubes\t\t')
#print(number0,' \t\t\t',square0,' \t\t\t\t', cube0)
#print(number1,' \t\t\t',square1,' \t\t\t\t', cube1)
#print(number2,' \t\t\t',square2,' \t\t\t\t', cube2)
#print(number3,' \t\t\t',square3,' \t\t\t\t', cube3)
#print(number4,' \t\t\t',square4,' \t\t\t\t', cube4)
#print(number1,' \t\t\t',square5,'  \t\t\t\t', cube5)
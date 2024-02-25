#(Separating the Digits in an Integer) Write a script that inputs a fivedigit
#integer from the user. Separate the number into its individual digits.
#Print them separated by three spaces each. For example, if the user types
#in the number 42339, the script should print
#4 2 3 3 9
#Assume that the user enters the correct number of digits. Use both the
#floor division and remainder operations to “pick off” each digit.


number = int(input('Enter a number: '))
first_number = number // 10000
second_number = number % 10000 // 1000
third_number = number % 1000 // 100
fourth_number = number % 100 // 10
fifth_number = number % 10

print(first_number, second_number, third_number, fourth_number, fifth_number)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(my_list)

for odd_numbers in my_list:
    if odd_numbers % 2 == 1:
        print(odd_numbers, end="    ")

        twice_of_odd_numbers = odd_numbers * 2
        print(twice_of_odd_numbers)

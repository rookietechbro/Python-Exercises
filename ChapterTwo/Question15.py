#(Sort in Ascending Order) Write a script that inputs three different
#floating-point numbers from the user. Display the numbers in increasing
#order. Recall that an if statement’s suite can contain more than one
#statement. Prove that your script works by running it on all six possible
#orderings of the numbers. Does your script work with duplicate numbers?
#[This is challenging. In later chapters you’ll do this more conveniently and
#with many more numbers.]

first_number = float(input("Enter your first decimal number:"))
second_number = float(input("Enter your second decimal number:"))
third_number = float(input("Enter your third decimal number:"))


#if first_number < second_number < third_number:
#   print(first_number < second_number < third_number)

#if second_number < first_number < third_number:
#   print(second_number < first_number < third_number)

#if third_number < first_number < second_number:
#   print(third_number < first_number < second_number)

#if  first_number > third_number < second_number:
#    print(first_number < third_number < second_number)

#if second_number < third_number < first_number:
#    print(second_number < third_number < first_number)

#if third_number < second_number < first_number:
#    print(third_number < second_number < first_number)


if first_number > second_number:
    first_number , second_number = second_number , first_number

if second_number > third_number:
    first_number , third_number = third_number , first_number

if second_number > third_number:
    second_number , third_number = third_number , second_number

print(first_number, "<", second_number, "<", third_number )


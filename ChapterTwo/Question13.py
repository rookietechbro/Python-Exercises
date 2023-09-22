#(How Big Can Python Integers Be?) We’ll answer this question later
#in the book. For now, use the exponentiation operator ** with large and
#very large exponents to produce some huge integers and assign those to
#the variable number to see if Python accepts them. Did you find any
#integer value that Python won’t accept?


#Solution

large_exponent = 2 ** 1000
print(large_exponent)

large_exponent_two = 2 ** 2000
print(large_exponent_two)

large_exponent_three = 2 ** 10000
print(large_exponent_three)

#very_large_exponent = 2 ** 20000
#print(very_large_exponent)
#ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit


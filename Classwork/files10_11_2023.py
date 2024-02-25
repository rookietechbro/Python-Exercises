# file = open("demo.txt", mode='w')
# file.write("Ope is a short girl\n")
# file.write("This is a short girl\n")
# file.write("Tobi is a sweet husband to Ope")
# file.close()

# The above is an old way of writing files.
# The best way is to use the 'with' and 'as' keywords.

# with open("demo.txt", mode='w') as file:
#     file.write("Ope is a short girl\n")
#     file.write("This is a short girl\n")
#     file.write("Tobi is a sweet husband to Ope")
#
# with open('demo.txt', mode='a') as file:
#     file.write("This is Cohort 18")
#
#
# with open('accounts.txt', mode='r') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
#     for record in accounts:
#         account, name, balance = record.split()
#         print(f'{account:<10}{name:<10}{balance:>10}')


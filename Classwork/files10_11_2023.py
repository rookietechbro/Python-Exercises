file = open("demo.txt", mode='w')
file.write("Ope is a short girl\n")
file.write("This is a short girl\n")
file.write("Tobi is a sweet husband to Ope")
file.close()

# The above is an old way of writing files.
# The best way is to use the 'with' and 'as' keywords.

with open("demo.txt", mode='w') as file:
    file.write("Ope is a short girl\n")
    file.write("This is a short girl\n")
    file.write("Tobi is a sweet husband to Ope")

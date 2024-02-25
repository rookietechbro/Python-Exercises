# Strings 3/11/2023

import re

print('We hold these truths...'.upper())
print('We hold these truths...'.lower())
print('We hold these truths...'.capitalize())

print("Onyii {}".format("Ejiofor"))
print("Hello. YES!".split("."))
print("This is good, I am overkilling this.".split(","))

print(re.split(r',\s*', '1,2,3,4,5,6,7,8'))

first_three = "abc"
result = "+".join(first_three)
print(result)

my_list = ["The", "fox", "jumped", "over", "the", "moon" ]
output = " ". join(my_list)
print(output)

s = "        Write    "
s = s.strip()
print(s)

shout = "All animals are equal, but some are more equal than the others"
shout = shout. replace("equal", "same")
print(shout)

print("animals".index("a"))

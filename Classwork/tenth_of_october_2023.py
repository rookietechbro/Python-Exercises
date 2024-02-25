my_playlist = []
names = ["arua", "joy", "qudus", "ope"]
names2 = ["israel"]
tuple1 = 1, 2, 3
tuple2 = 'a', 'b', 'c'


list_to_tuple = tuple(names)
#print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
#print(tuple_to_list)

#print(names2)

#names += "israel"
#print(names)

#names[0] = "tosin"
#print(names)

#tuple1[0] = 'p'

tuple3 = 1, 2, 3, "ope", "delighted", True, ["precious", "joy"], "delighted"
#tuple3[4][0] = "mercy"
#print(tuple3)

tuple3 = 1, 2, 3, "ope",["precious", "joy"], "delighted"
lt = list(tuple3)
lt[3] = "tobi"
lt[3] = tuple(lt)
print(lt)


x, *others, y = tuple1
print(x, y, others)

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers *= 2
#print(numbers)
#print(numbers.index(2))
names.pop()
names.pop(0)
names.remove('arua')
print(names)
#del names[:]




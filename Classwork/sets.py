my_set = {1, 1.1, "ope", 1, 2, "ope"}
my_set2 = frozenset(my_set)
empty_set = set()
print(my_set)
print(empty_set)
print(len(my_set))
print(len(empty_set))

empty_set.add(4)
empty_set.add("delighted")
print(empty_set)
print(2 in my_set)

for item in my_set:
    print(item, end=' ')

my_set.pop()
print(my_set)

my_set.copy()
print(my_set)

set1 = set(range(1, 21))
set2 = {1, 4, 3, 5}
print(set1.issuperset(set2))
print(set2.issubset(set1))

print(set1 | set2) # union of both sets without duplicates
print(set1.union(set2))  # still the union of both sets without duplicates
print(set1 & set2)  # intersection of both sets i.e what's common with the two sets
print(set1.intersection(set2)) # still the intersection of both sets i.e what's common with the two sets

set1 = {1, 2, 6, 3, 7, 9}
set2 = {1, 4, 3, 5}
print(set1 - set2)  # difference in both sets i.e. elements that are in set1 but not in set2
print(set1.difference(set2))
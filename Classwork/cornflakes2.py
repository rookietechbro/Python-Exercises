# Write a python script to sort(ascending and descending) a dictionary by value.
# Sample input = {2: 4, 1: 3, 3: 9, 5: 25, 4: 16}
# Sample output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

sample_input = {2: 4, 1: 3, 3: 9, 5: 25, 4: 16}
sorted_dict = dict(sorted(sample_input.items()))
print(sorted_dict)


def add_key_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary


print(add_key_value(sample_input, 6, 36))


def add_key_value(dictionary, key, value):
    dictionary.update({key: value})
    return dictionary
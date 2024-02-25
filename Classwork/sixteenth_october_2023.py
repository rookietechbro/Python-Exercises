my_list = []

for i in range(2):
    for j in range(3):
        my_list.append(i * j)
        print(f'[{i}] [{j}] = {i * j}', end='')
    print()
print(my_list)
total = 0
grade_counter = 0

for scores in [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]:
    total += scores
    grade_counter += 1

    average = total / grade_counter
print("Average is", average)

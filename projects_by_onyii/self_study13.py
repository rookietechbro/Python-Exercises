students_grades_list = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
grades_total = 0
grades_counter = 0

for students_grades in students_grades_list:
    grades_total += students_grades
    grades_counter += 1

average = grades_total / grades_counter
print(f'Class_average is {average}')
print(f'Class_average is {average:.0f}')
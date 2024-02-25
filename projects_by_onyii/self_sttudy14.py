grades_total = 0
grades_counter = 0
student_grade = int(input("Enter the grade between -1 till the end: "))

while student_grade != -1: #sentinel control.
    grades_total += student_grade
    grades_counter += 1
    student_grade = int(input("Enter the grade between -1 to the end: "))

    if grades_counter != 0: #trying to avoid a run-time error from dividing by 0.
        class_average = grades_total / grades_counter
        print(f'Class average is {class_average: .2f}.')
    else:
        print("No grade was entered.")


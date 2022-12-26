name = input()
class_number = 1
bad_tries = 0
grades = 0
while class_number <= 12:
    grade = float(input())
    if grade >= 4:
        class_number += 1
        grades += grade
    else:
        bad_tries += 1
    if bad_tries == 2:
        break
average_grade = grades / 12

if bad_tries == 2:
    print(f"{name} has been excluded at {class_number} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

bad_grade = int(input())
command = input()
bad_tries = 0
number_of_comands = 0
grades = 0
last_problem = ''
while command != "Enough":
    grade = int(input())
    number_of_comands += 1
    grades += grade
    last_problem = command
    if grade <= 4:
        bad_tries += 1





    if bad_tries == bad_grade:
        break




    command = input()
average = grades / number_of_comands
if bad_tries != bad_grade:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {number_of_comands}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_tries} poor grades.")
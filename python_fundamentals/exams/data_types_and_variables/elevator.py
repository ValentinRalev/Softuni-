number_of_people = int(input())
capacity = int(input())
courses = 0
if number_of_people % capacity == 0:
    courses = int(number_of_people / capacity)
else:
    courses = int(number_of_people / capacity) + 1
print(courses)

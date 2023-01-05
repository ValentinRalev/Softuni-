students = int(input())
student_grades = {}

for _ in range(students):
    name, grade = input().split()
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(float(grade))
for key, avg in student_grades.items():
    print(f"{key} -> ", end="")
    for k in avg:
        print(f"{k:.2f}", end=" ")
    print(f"(avg: {(sum(avg) / len(avg)):.2f})")

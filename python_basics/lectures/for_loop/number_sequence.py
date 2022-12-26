import sys

number = int(input())
maxnumber = -sys.maxsize
minnumer = sys.maxsize
for i in range(number):
    current_number = int(input())
    if current_number > maxnumber:
        maxnumber = current_number
    if current_number < minnumer:
        minnumer = current_number
print(f"Max number: {maxnumber}")
print(f"Min number: {minnumer}")
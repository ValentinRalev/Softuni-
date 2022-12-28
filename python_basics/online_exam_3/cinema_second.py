capacity = int(input())
input_line = input()
sum = 0
count = capacity
is_full = False
while input_line != "Movie time!":
    is_full = True
    price = 0
    people = int(input_line)
    if count < people:
        break
    count = count - people

    price = people * 5
    if people % 3 == 0:
        price = price - 5

    sum += price

    input_line = input()
if input_line != "Movie time!" and count >= 0:
    print("The cinema is full.")

else:
    print(f"There are {count} seats left in the cinema.")
print(f"Cinema income - {sum} lv.")
n = int(input())
n2 = int(input())
magic_number = int(input())

tries = 0
is_found = False
for number in range(n, n2 +1):
    for second_number in range(n, n2 +1):
        tries += 1
        if number + second_number == magic_number:
            is_found = True

            break
    if is_found == True:
        break


if is_found:
    print(f"Combination N:{tries} ({number} + {second_number} = {magic_number})")
else:
    print(f"{tries} combinations - neither equals {magic_number}")
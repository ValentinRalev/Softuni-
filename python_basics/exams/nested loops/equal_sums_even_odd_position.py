number_one = int(input())
number_two = int(input())
for numbers in range(number_one, number_two +1):
    current_num = str(numbers)
    even_sum = 0
    odd_sum = 0
    for i in range(0, len(current_num)):
        digit = int(current_num[i])
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(numbers, end= " ")


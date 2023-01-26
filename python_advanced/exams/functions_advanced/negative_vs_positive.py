def total_sum(*args):
    sum_of_num = 0
    for el in args:
        sum_of_num += el
    return sum_of_num


sequence_of_numbers = [int(x) for x in input().split()]
positive = [x for x in sequence_of_numbers if x > 0]
negative = [x for x in sequence_of_numbers if x < 0]
sum_of_positive = total_sum(*positive)
sum_of_negative = total_sum(*negative)
print(sum_of_negative)
print(sum_of_positive)
if sum_of_positive > abs(sum_of_negative):
    print("The positives are stronger than the negatives")
elif sum_of_positive < abs(sum_of_negative):
    print("The negatives are stronger than the positives")

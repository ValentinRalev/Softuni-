number = int(input())
longest_len = 0
result = set()
for _ in range(number):
    first, second = input().split("-")
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(y) for y in second.split(",")]
    first_set = set()
    second_set = set()
    for nums in range(first_start, first_end + 1):
        first_set.add(nums)
    for nums in range(second_start, second_end + 1):
        second_set.add(nums)
    res = first_set.intersection(second_set)
    if longest_len < len(res):
        longest_len = len(res)
        result = res
print(f"Longest intersection is [{', '.join(str(x) for x in result)}] with length {longest_len}")

n = int(input())
sum_of_chars = 0
for _ in range(n):
    letter = input()
    sum_of_chars += ord(letter)
print(f"The sum equals: {sum_of_chars}")

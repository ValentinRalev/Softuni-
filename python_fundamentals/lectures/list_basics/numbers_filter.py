n_lines = int(input())
even = []
odd = []
positive = []
negative = []
for i in range(n_lines):
    number = int(input())
    if number >= 0:
        positive.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    else:
        negative.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
word = input()
if word == "even":
    print(even)
elif word == "odd":
    print(odd)
elif word == "positive":
    print(positive)
else:
    print(negative)

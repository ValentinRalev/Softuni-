n_lines = int(input())
word = input()
new_list = []
for i in range(n_lines):
    new_word = input()
    new_list.append(new_word)
print(new_list)
filtered_list = []
for index in new_list:
    if word in index:
        filtered_list.append(index)
print(filtered_list)

some_text = input()
unique_text = set()
for char in some_text:
    unique_text.add(char)
sorted_text = sorted(unique_text)
for el in sorted_text:
    print(f"{el}: {some_text.count(el)} time/s")

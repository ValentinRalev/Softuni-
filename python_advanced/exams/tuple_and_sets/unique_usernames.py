number = int(input())
usernames = set()
for _ in range(number):
    user = input()
    usernames.add(user)
print("\n".join(usernames))
from collections import deque

name = input()
served_client = deque()
while name != "End":
    if name == "Paid":
        while served_client:
            print(served_client.popleft())
    else:
        served_client.append(name)
    name = input()
print(f"{len(served_client)} people remaining.")
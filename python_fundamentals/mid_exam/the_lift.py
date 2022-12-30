people = int(input())
lift = [int(x) for x in input().split()]
for num in range(len(lift)):
    load = min(4 - lift[num], people)
    lift[num] += load
    people -= load

result = " ".join([str(x) for x in lift])
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([x for x in lift if x < 4]) > 0:
    print(f"The lift has empty spots!")
print(result)

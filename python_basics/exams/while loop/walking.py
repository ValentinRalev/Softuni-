steps = input()
sum_steps = 0
while steps != "Going home":
    current_step = int(steps)
    sum_steps += current_step
    if sum_steps >= 10000:
        break




    steps = input()

if steps == "Going home":
    current_step_home = int(input())
    sum_steps += current_step_home
diff = abs(10000 - sum_steps)

if sum_steps < 10000:
    print(f"{diff} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
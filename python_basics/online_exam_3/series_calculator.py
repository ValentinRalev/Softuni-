import math
name = input()
seasons = int(input())
episodes = int(input())
time_episode = float(input())
special_episode = 10
time_add = time_episode * 1.20
all_time = seasons * (episodes * time_add + special_episode)
print(f"Total time needed to watch the {name} series is {math.floor(all_time)} minutes.")

time_pictures = int(input())
scenes = int(input())
time_scene = int(input())
prep_time = 0.15 * time_pictures
time_movie = scenes * time_scene + prep_time
diff = abs(time_pictures - time_movie)
if time_movie <= time_pictures:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
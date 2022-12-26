exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())
time_exam = exam_hours * 60 + exam_minutes
arrival_time = arrival_hours * 60 + arrival_minutes
diff = abs(arrival_time - time_exam)
hours = 0
minutes = 0
if arrival_time > time_exam:
    print("Late")
    if diff > 59:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    elif diff <= 59:
        minutes = diff
        print(f"{minutes} minutes after the start")
elif arrival_time <= time_exam and diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
elif arrival_time < time_exam and diff > 30:
    print("Early")
    if diff <= 59:
        print(f"{diff} minutes before the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")



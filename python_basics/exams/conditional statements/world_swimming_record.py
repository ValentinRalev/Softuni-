from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_meter_sec = float(input())
time_waste = floor(distance_meters / 15)
time_waste_seconds = time_waste * 12.5
new_time = distance_meters * time_meter_sec + time_waste_seconds
diff = abs(record_seconds - new_time)
if new_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
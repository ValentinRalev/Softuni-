import sys

number_snowballs = int(input())
snowball_max = -sys.maxsize
snow_time_max = -sys.maxsize
snow_quality_max = -sys.maxsize
snow_snow_max = -sys.maxsize

for n in range(number_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > snowball_max:
        snowball_max = snowball_value
        snow_snow_max = snowball_snow
        snow_time_max = snowball_time
        snow_quality_max = snowball_quality


print(f"{snow_snow_max} : {snow_time_max} = {snowball_max} ({snow_quality_max})")

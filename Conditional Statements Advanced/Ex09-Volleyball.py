from math import floor

year_type = input()
holiday_count_non_weekend = int(input())
amount_weekend_travel_to_home_city = int(input())

#48 weekends per year
#Volleyball on weekends and holidays
#Volleyball every Saturday when not going to home city and not working
#Also on 2/3 of holiday days
#Go a certain amount of weekends to home city and play volleyball with old friends on Sundays while there
#Not working during 3/4 of weekends
#During leap yers, 15% more volleyball play
#Conclusion: Assume "normal" year is default. Use if statement only for "leap" years to add an additional 15% volleyball play
#Very Important: Those weekends at homce city do not count towards those 1/4 of working weekends
#Conclusion: Subtract the home city weekends from the normal weekends. Then add them again after subtracting the working weekends

opportunities_to_play_volleyball = 48 #Start with a base of 48 because of total weekends per year

opportunities_to_play_volleyball -= amount_weekend_travel_to_home_city

holiday_plays = holiday_count_non_weekend * (2/3)

opportunities_to_play_volleyball -= opportunities_to_play_volleyball * (1/4)
opportunities_to_play_volleyball += holiday_plays
opportunities_to_play_volleyball += amount_weekend_travel_to_home_city

if year_type == "leap":
    opportunities_to_play_volleyball += opportunities_to_play_volleyball * 0.15

opportunities_to_play_volleyball = floor(opportunities_to_play_volleyball)

print(opportunities_to_play_volleyball)




from math import floor

world_record_secs = float(input())
distance_meters = float(input())
time_to_cross_one_meter_secs = float(input())

time_slowed_by_water_resistance = floor(distance_meters / 15) * 12.5

pool_cross_time = distance_meters * time_to_cross_one_meter_secs + time_slowed_by_water_resistance

if(pool_cross_time < world_record_secs):
    print(f"Yes, he succeeded! The new world record is {pool_cross_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(world_record_secs - pool_cross_time):.2f} seconds slower.")
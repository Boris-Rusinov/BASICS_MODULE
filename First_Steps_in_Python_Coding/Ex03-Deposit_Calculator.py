dep_sum = float(input())
dep_duration = int(input())
annual_interest_rate = float(input())

dep_end_sum = dep_sum + dep_duration * ((dep_sum * annual_interest_rate / 100) / 12)

print(dep_end_sum)
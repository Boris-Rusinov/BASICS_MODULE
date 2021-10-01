aquarium_length_cm = int(input())
aquarium_width_cm = int(input())
aquarium_height_cm = int(input())
percent_volume_already_taken = float(input())

parallelepiped_volume_cubic_decimeteres =  aquarium_length_cm * aquarium_width_cm * aquarium_height_cm / 1000

volume_in_litres = parallelepiped_volume_cubic_decimeteres - parallelepiped_volume_cubic_decimeteres * (percent_volume_already_taken / 100)

print(volume_in_litres)


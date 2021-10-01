import math

figure_type = input()

if(figure_type == "square"):
    a = float(input())
    area = a * a
elif(figure_type == "triangle"):
    a = float(input())
    height = float(input())
    area = a * height / 2
elif(figure_type == "rectangle"):
    a = float(input())
    b = float(input())
    area = a * b
elif(figure_type == "circle"):
    r = float(input())
    area = r * r * math.pi

print(f"{area:.3f}")
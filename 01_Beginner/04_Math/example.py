import math

a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = math.sqrt(a**2 + b**2)

print(f"Hypotenuse is {c}")

# ---

radius = float(input("Enter the radius of a circle:"))
area= math.pi * radius**2
print(f"The area of the circle is {area}")


#  ---

a = 9.7
total = math.ceil(a)
print(total)

# ---

radius = float(input("Enter the radius of a circle:"))
area = math.pi * radius**2
area_rounded= round(area,0)
print(f"The area of the circle is {area_rounded}")




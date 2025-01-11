import math
print ("This program will find area and circumference of a circle")
radius = float(input("Please input the circle\'s radius: "))
area = math.pi * radius * radius;
circum = 2 * math.pi * radius
print ("The area is: ",area)
print ("The circumference is: ",circum)

#1 - Write a Python program to convert degree to radian.
"""
import math

def degreeToRadian(degrees):
    return degrees * math.pi / 180

degrees = int(input("Input degree: "))
radians = degreeToRadian(degrees)

print("Output radian: ", radians)
"""

#2 - Write a Python program to calculate the area of a trapezoid.
"""
def area(base, base2, height):
    return 0.5 * (base + base2) * height

height = int(input("Height: "))
base = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))

areaOfTrapezoid = area(base, base2, height)

print("Expected Output: ", areaOfTrapezoid)
"""

#3 - Write a Python program to calculate the area of regular polygon.
"""
import math

def area(num, length):
    return (num * length**2) / (4 * math.tan(math.pi / num))

num = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

areeOfPolygon = area(num, length)

print("The are of the polygon is: ", int(areeOfPolygon))
"""

#4 - Write a Python program to calculate the area of a parallelogram.
"""
def area(base, height):
    return base * height

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

areaOfParallelogram = area(base, height)

print("Expected Output: ", float(areaOfParallelogram))
"""
#Write a Python program which accepts the radius of a circle from the user
# and compute the area.
# Sample input: Enter the radius: 3
# Sample output: Area of Circle is 28.5999999999
import math
pi = math.pi
radius = float(input('enter the radius: '))
area = pi * radius **2
print(area)
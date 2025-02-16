import math
 
num_of_sides = float(input("Input number of sides: "))
length_of_side = float(input("Input the length of a side: "))

area_of_polygon = (num_of_sides * (length_of_side ** 2)) / (4 * math.tan(math.pi / num_of_sides))
print(f'The area of the polygon is: {area_of_polygon}') 
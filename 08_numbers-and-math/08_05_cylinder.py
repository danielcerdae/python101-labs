# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

import math

radius = 3.14

height = 5

perimeter = 2 * math.pi * radius

area = round(perimeter * height, 2)

volume = round(area * height,2)

print(f'Volume = {volume}, Surface Area = {area}')
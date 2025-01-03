## Calculate the area of a Circle, Rectangle and Triangle
import math
## Area of circle
radius_circle = float(input("Enter the radius of the circle"))
area_circle = math.pi * radius_circle * radius_circle
print(area_circle)
##Area of Rectangle
length_rectangle = float(input("Enter the length of a rectangle: "))
width_rectangle = float(input("Enter the width of the rectangle:  "))
area_rectangle = length_rectangle * width_rectangle
print(area_rectangle)

## area of triangle
base_triangle = float(input("Enter the base of the triangle:"))
height_triangle = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base_triangle * height_triangle
print(area_triangle)



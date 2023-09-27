"""
Chapter 1 Exercise 5 Compute area of a circle
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""
radius = float(input("Enter the radius of the circle: "))  #Radius of the circle

area = 3.14159 * (radius ** 2) #Calculate the area

print(f"The area of the circle with radius {radius} is {area:.2f}") #print the result

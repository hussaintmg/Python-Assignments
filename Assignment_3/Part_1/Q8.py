#Write a function to compute the area and circumference of the circle and return the computed results.
def Area(val):
  return f"Area of Circle = {3.142*(val**2)}"
def CIrcum(val):
  return f"Circumference of Circle = {2*3.142*val}"
number=int(input("Enter Radius: "))
print(Area(number))
print(Circum(number))

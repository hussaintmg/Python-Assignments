#Write a program that takes a temperature in Celsius and checks if it is freezing, moderate or hot.
temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp < 26:
    print("Moderate")
else:
    print("Hot")

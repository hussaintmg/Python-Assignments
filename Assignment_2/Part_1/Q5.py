#Check whether a citizen is minor, adult or senior citizen

age = int(input("Enter Your Age: "))
if age<18:
  print("You are a Minor Citizen")
elif age>18 and age<=60:
  print("You are a Adult Citizen")
else :
  print("You are a Senior Citizen")

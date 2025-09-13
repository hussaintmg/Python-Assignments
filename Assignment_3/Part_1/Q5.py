#Write a function to take user’s age as argument and return the message from the function whether he is minor, adult or senior citizen:
def citizen(age):
  if age > 60:
    return "Your are a Senior Citizen"
  elif age> 18:
    return "Your are a Adult Citizen"
  else"
    return "Your are a Minor Citizen"

age = int(input("Enter Your Age: "))
cit=citizen(age)
print(cit)

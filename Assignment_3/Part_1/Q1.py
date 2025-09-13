#Write a function named “Greetings” that takes user’s name and print greeting.
#Output:       Welcome to SMIT training center, Ahsan 

def Greeting(name):
  return f"Welcome to SMIT training center, {name}"

name = input("Enter Your Name: ")
greet=Greeting(name)
print(greet)

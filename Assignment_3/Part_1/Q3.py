#Write a function to take two numbers as arguments and return the larger number.

def compare(num1 , num2):
  if num1>num2:
    return "Numer 1 is Greater than Number 2"
  else:
    return "Numer 2 is Greater than Number 1"

num1=int(input("Enter Number 1: "))

num2=int(input("Enter Number 2: "))

comp=compare(num1,num2)
print(comp)

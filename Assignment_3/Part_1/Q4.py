#Write a function to take three numbers as argument and return the largest number.
def Compare(num1,num2,num3):
  if num1>num2 and num2>num3:
    return "Number 1 is the larger number"
  elif num2>num1 and num1>num3:
    return "Number 2 is the larger number"
  else:
    return "Number 3 is the larger number"
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
comp =Compare(num1,num2,num3)
pront(comp)

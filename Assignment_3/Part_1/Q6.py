#Write a function to take integer as argument and check if it is even or odd.
def number(num):
  if num%2==0:
    return "Number is Positive"
  else:
    return "Number is Odd"

num=int(input("Enter a Number: "))
numb=number(num)
print(numb)

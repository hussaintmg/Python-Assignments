#Write a function that takes a number as argument and check if a given number is positive, negative or zero.
def number(num):
  if num>0:
    return "Number is Positive"
  elif num<0:
    return "Number is Negative"
  else:
    return "Number is Zero"
numb = int(input("Enter Number: "))
num=number(numb)
print(num)

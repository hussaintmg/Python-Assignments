#Write a program that ask for an integer number and checks if it is divisible by 2, 3, or both.
num=int(input("Enter Number: "))
if num%2==0 and num%3==0:
  print("Number is Divisible By Both 2 and 3")
if num%2==0 and num%3!=0:
  print("Number is Divisible By 2")
if num%2!=0 and num%3==0:
  print("Number is Divisible By 3")
else:
  print("Number is not Divisible by Both 2 and 3")

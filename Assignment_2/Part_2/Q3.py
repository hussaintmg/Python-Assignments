#Write a program to print multiplication table of a given number.
num=int(input("Enter a Number: "))
for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

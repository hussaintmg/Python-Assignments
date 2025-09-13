#Write a program to take two numbers and an operator (/,x,+,-) as input and perform the corresponding operation.
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
oper=input("Enter operator")
if oper=="+":
  print(f"{num1} + {num2} = {num1+num2}")
if oper=="-":
  print(f"{num1} - {num2} = {num1-num2}")
if oper=="*":
  print(f"{num1} * {num2} = {num1*num2}")
if oper=="/":
  print(f"{num1} / {num2} = {num1/num2}")
else:
  print("Please Enter a valid operator(+,-,*,/)")

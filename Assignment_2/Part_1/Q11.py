#Write a program that evaluates if an input number is prime.
num = int(input("Enter Number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a  Prime number")
            break
    else:
        print(f"{num} is Prime number .")
else:
    print(f"{num} is not a Prime Number.")

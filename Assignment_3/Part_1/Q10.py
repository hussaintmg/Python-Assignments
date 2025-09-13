#Write a function that evaluates if an input number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# User input
number = int(input("Enter a number: "))
if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")

#Write a program to calculate the sum of even and odd numbers and print them. (numbers from 1 to 50)
even_sum = 0
odd_sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

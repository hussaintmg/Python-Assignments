# Q.1:Arithmetic Operators
a = 10
b = 5
print(f"Addition: {a} + {b} =", a + b)

print(f"Subtraction: {a} - {b} =", a - b)

print(f"Multiplication: {a} * {b} =", a * b)

print(f"Division: {a} / {b} =", a / b)

print(f"Floor Division: {a} // {b} =", a // b)

print(f"Modulus: {a} % b =", a % b)

print(f"Exponentiation: {a} ** {b} =", a ** b)



#Q.2: Arithmetic Assignment Operators
x = 10
print("Initial value of x:", x)
x += 5
print("After x += 5:", x)
x *= 2
print("After x *= 2:", x)
x -= 4
print("After x -= 4:", x)
x /= 2
print("After x /= 2:", x)



#Q.3: Comparison Operators
a = 7
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


#Q.4: Which comparisons return True?
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


#Q.5: Membership Operators
institute = "Saylani Mass IT"

print("’s’ in institute:", "s" in institute)
print("'Saylani' in institute:", "Mass" in institute)
print("'Saylani' not in institute:", "Saylani" not in institute)


#Q.6: Identity Operators
a = 15
b = 15
c = 200
print("a is b:", a is b)
print("a is c:", a is c)
print("c is not b:", c is not b)


#Bonus Challange

# Take username and password input from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Compare with predefined username and password
if username == "Talha" and password == "Axiom123":
    print("Login successful!")
else:
    print("Invalid username or password.")

#Write a program that continues to ask user to input password until the correct password is entered.
correct_password = "1234"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password, try again.")

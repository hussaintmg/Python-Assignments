#Write a program to take user’s score as input and determine if they pass or fail (pass if score is above 60, otherwise fails.)
score = int(input("Apna score enter karein: "))

if score > 80 and score <= 100:
    print("Grade: A+")
elif score >= 70 and score <= 80:
    print("Grade: A")
elif score >= 60 and score <= 70:
    print("Grade: B")
elif score >= 50 and score <= 60:
    print("Grade: C")
elif score >= 40 and score <= 50:
    print("Grade: D")
else:
    print("Fail")

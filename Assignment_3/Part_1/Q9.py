#Write a function to take user’s score as argument and determine if they pass or fail (pass if score is above 60, otherwise fails.)
def check_result(score):
    if score > 60:
        return "Pass"
    else:
        return "Fail"

user_score = int(input("Enter your score: "))
result = check_result(user_score)
print(result)

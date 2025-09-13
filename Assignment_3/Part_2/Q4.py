#Write a code to get first and second best scores from the list
Scores_list = [40, 89, 90, 89, 23, 90, 50]

Scores_list.sort(reverse=True)

first_best = Scores_list[0]
second_best = Scores_list[1]

print("First best score:", first_best)
print("Second best score:", second_best)

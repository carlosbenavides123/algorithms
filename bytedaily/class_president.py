# High school students are voting for their class president
# and you’re tasked with counting the votes. Each presidential candidates is represented by a unique integer
# and the candidate that should win the election is the candidate that has received more than half the votes.
# Given a list of integers, return the candidate that should become the class president.
# Note: You may assume there is always a candidate that has received more than half the votes.

# Ex: Given the following votes…

# votes = [1, 1, 2, 2, 1], return 1.
# Ex: Given the following votes…

# votes = [1, 3, 2, 3, 1, 2, 3, 3, 3], return 3.

# [1, 2, 3] would never be a input
# [1, 1, 2] would be a input
# [1, 2] would never be a input

# [2, 1, 1]
# KICK 2, cand = 1

# [1, 3, 2, 3, 1, 2, 3, 3, 3]
# candidate = 1, count = 1
# i = 1, count -= 1
# kick 1
# i = 2
# cand = 2, count = 1
# i = 3, count -= 1
# kick 2
# i = 4, cand = 1, count = 0
# ..

def class_president(votes):
    cand = votes[0]
    count = 1
    for vote in votes[1:]:
        if count == 0:
            cand = vote
            count = 1
        elif cand == vote:
            count += 1
        else:
            count -= 1
    return cand

votes = [1, 3, 2, 3, 1, 2, 3, 3, 3]
print(class_president(votes))

votes = [1, 1, 2, 2, 1]
print(class_president(votes))

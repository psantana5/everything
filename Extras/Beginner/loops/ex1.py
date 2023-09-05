#You have a list of votes that are either "yes" or "no". Count the number of "yes" and "no" votes.

votes = ["yes", "no", "yes", "yes", "no", "yes", "no", "no"]

yes_count = 0
no_count = 0

for vote in votes:
    if vote == "yes":
        yes_count += 1
    elif vote == "no":
        no_count += 1

print("Yes votes:", yes_count)
print("No votes:", no_count)

#Exercise 5: Element Search - Find All Occurrences
#You have a list of grades and you want to find out all the indices where the grade is 'A'.

grades = ['A', 'B', 'C', 'A', 'D', 'A', 'F']

indices_of_A = []


for index, grade in enumerate(grades):
    if grade == 'A':
        indices_of_A.append(index)

print("The indices of A's are:", indices_of_A)
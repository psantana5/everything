#Exercise 6: Multiplication Table Generator
#Generate a multiplication table for a given number. This is useful for educational software.

n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")  
    print()  
#Exercise 7: Factorial Calculation
#Calculate the factorial of a number. This has applications in mathematics and statistics.

n = 6 #Calculate 6!

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")

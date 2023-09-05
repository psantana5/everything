#Exercise 3: Data Aggregation - Average Temperature
#Calculate the average temperature from a list of daily temperatures.

temperatures = [68, 70, 75, 79, 80, 79, 71]

sum_all = 0

for temperature in temperatures:
    sum_all += temperature

final_result = sum_all / len(temperatures)
     
print("The average temperature is:", final_result)
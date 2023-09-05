#Exercise 2: Summation Loop - Calculate Total Price
#You have a list of item prices. Calculate the total price.

prices = [12.50, 3.79, 6.20, 19.99]

final_price = 0

for price in prices:
    final_price += price

print(f"The total price is:", final_price)
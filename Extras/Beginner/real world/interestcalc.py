

principal = 280.000 # in thousands of USD
interest = 0.05 # percent
time = 10 # years

simple_interest = principal * interest * time


for time in range(1, 11):
    simple_interest = principal * interest * time
    amount = principal + simple_interest
    print(f"The amount of money after year {time} is ${amount:.2f}")
    principal = amount
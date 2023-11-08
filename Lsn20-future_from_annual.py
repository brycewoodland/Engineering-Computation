
print('This program will calculate the future value of a one-time present investment.')
print()
annual_investment = float(input('How much is the annual investment (in dollars)? \n'))
annual_interest_rate = float(input('What is the annual interest rate (enter 0.05 for 5%)? \n'))
annual_interest_percent = annual_interest_rate*100
time = float(input('How long is the investment (in years)? \n'))
future_value = annual_investment*((1 + annual_interest_rate)**time-1)/(annual_interest_rate)
print(f'${annual_investment:.2f} deposited each year at {annual_interest_percent:.2f}% annual interest will be worth ${future_value:.2f} in {time} years.')

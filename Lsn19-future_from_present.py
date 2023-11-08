"""
This program will calculate the future 
value of a one-time present investment.
"""
one_time_investment = float(input('How much is the one-time present investment (in dollars)? \n'))
annual_interest_rate = float(input('What is the annual interest rate (enter 0.05 for 5%)? \n'))
annual_interest_percent = annual_interest_rate*100
time = input('How long is the investment (in years)? \n')
future_value = one_time_investment*(1 + annual_interest_rate)**float(time)
print(f'\n ${one_time_investment:.2f} deposited now at {annual_interest_percent:.2f}% will be worth ${future_value:.2f} in {time} years. \n')

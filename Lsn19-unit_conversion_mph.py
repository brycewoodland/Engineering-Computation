""""
File: Unit_Conversion.py
Author: Bryce Woodland
Date: 10/27/22
Purpose: convert speed in ft/sec to speed in miles/hr
"""

# Known information
ft_in_miles = 5280
sec_in_min = 60
min_in_hr = 60

# Get speed in ft/sec from the user
print()
ft_per_sec = input('\nWhat is the speed in ft/sec ')

# Conver speed to miles / hour
miles_per_hour = float(ft_per_sec)/ft_in_miles*sec_in_min*min_in_hr

# Display speed in miles / hour
print(f'That speed is {miles_per_hour} miles / hour.\n')
print()
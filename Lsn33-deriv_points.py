'''
File: deriv_points.py
Author: Bryce Woodland
Date: 12/4/2022
Purpose: Approximate the derivative 
of a set of data points
'''
import matplotlib.pyplot as plt

# Define the data points
x = [1,2.5,4]
y = [6,10,12]

slope = []
# Approximate the derivative at each point
for i in range(len(x)):
    if i == 0:
        # Use the forward difference approach 
        deriv = (y[i+1]-y[i])/(x[i+1]-x[i])
        slope.append(deriv)
    elif i == len(x)-1:
        # Use the backward difference approach
        deriv = (y[i]-y[i-1])/(x[i]-x[i-1])
        slope.append(deriv)
    else:
        # Use the centered difference approach
        deriv = (y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        slope.append(deriv)

# Print results
print('\nTime (s)    Position (ft)   Velocity (ft/s)')
for i in range(len(x)):
    print(f'{x[i]:5.1f} {y[i]:11.1f} {slope[i]:14.2f}')
print()

# Plot results
plt.plot(x,y, '-bo', label = 'Position (ft)')
plt.grid(True)
plt.plot(x,slope,'-ro', label = 'Velocity (ft/s)')
plt.legend(loc = 'right')
plt.xlabel('Time (s)')
plt.title('Plot of position and velocity over time')
plt.xlim(0,16)
plt.ylim(0,30)
plt.show()

import numpy as np
# Experiment with numpy functions arange and linspace
# x1 = np.linspace(0,10,11)
# x2 = np.arange(0,11,1)
# print(x2)

import matplotlib.pyplot as plt
# x = [0,1,2,3,4,5]
# y = [0,2,8,20,45,80]
# plt.plot(x,y)
# plt.show()


# Plot a quadratic function
# x = np.linspace(0,5,100)
# # x = np.arange(0,5.1,.1)
# y = 4*x**2 - 6*x + 9

# # plt.plot(x,y,linestyle = '-', color = 'r', marker = '.')
# plt.plot(x,y, '-r')
# plt.title('Plot of Quadratic Function')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.grid(True)
# plt.show()

# Plot multiple series
k = 2 # lbs / in
x = np.linspace(0,2,10)
y = k*x
x_data = [.3, .8, 1, 1.4, 2]
y_data = [0.8, 1.4, 2.1, 2.5, 3.2 ]
plt.plot(x_data,y_data, 'bo', label = 'Data Points')
plt.plot(x,y, 'r',label = 'Equation')
plt.title('Spring Behavior', size = 12, weight = 'bold')
plt.xlabel('Displacement (in.)')
plt.ylabel('Force (lbs)')
plt.legend(loc = 'right')
plt.grid(True)
plt.xlim(0,2.5)
plt.ylim(0,5)
plt.xticks([0,0.5,1,1.5,2,2.5])
plt.yticks([0,1,2,3,4,5])
plt.show()

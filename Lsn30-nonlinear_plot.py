import matplotlib.pyplot as plt
import numpy as np

p = 1.23
A = 0.01
CD = 0.47
x = np.linspace(0,23,24)
y = 0.5*p*A*CD*x**2
x_data = [0,3,8,12,15,20,23]
y_data = [0,0.03,0.12,0.35,0.7,1.25,1.3]


plt.plot(x_data,y_data,'bo', label = 'Data Points')
plt.plot(x,y, 'r-', label = 'Equation')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8])
plt.xticks([0,5,10,15,20,25])
plt.xlabel('v (m/s)')
plt.ylabel('F,drag (N)')
plt.title('Drag Force Example', size = 12, weight = 'bold' )
plt.grid(True)
plt.legend(loc = 'lower right')
plt.xlim(0,25)
plt.ylim(0.0,1.8)
plt.show()

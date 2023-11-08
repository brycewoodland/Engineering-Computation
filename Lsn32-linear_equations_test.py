import numpy as np
a = np.zeros(5)
print(a)

b = np.ones((2,3))
print(b)

a[3]=5
print(a)

print(a[0])
print(a[3])

b[0,1] = 15
print(b)

print(b[1,1])
print(b[0,1])

x = np.array([1,2,3,4,5])
print(x[2])

x[2] = 10
print(x)

y = np.array([[1,2,3,],[4,5,6]])
print(y[1,2])

y[1,2] = 25
print(y)
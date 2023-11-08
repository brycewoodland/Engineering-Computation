# approximate the integral of an equation
# using the trapezoidal rule

# Store the equation in a Python function
def my_fun(x):
    value_of_equation = 3*x**3 + 4*x**2 + 5*x + 7
    return value_of_equation 

# Integrate the equation from 0 to 5

# Single trapezoid
trap_area = (4-0)*(my_fun(0)+my_fun(4))/2
print(f'\nUsing 1 trapezoid, the integral is approximately {trap_area:.1f}')

# Two trapezoids
trap1_area = (2.5-0)*(my_fun(0)+my_fun(2.5))/2
trap2_area = (5-2.5)*(my_fun(2.5)+my_fun(5))/2
total_area = trap1_area + trap2_area
print(f'Using 2 trapezoids, the integral is approximately {total_area:.1f}\n')

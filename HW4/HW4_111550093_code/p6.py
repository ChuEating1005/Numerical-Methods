import numpy as np

# Define the function to be integrated
def f(x, y):
    return (x - 1)**2 + y**2 / 16

# Define the limits of the region
x_min, x_max = -2, 3
y_min, y_max = -1, 2

# Define the number of random points
num_points = 1000000

# Generate random points in the region R
x_random = np.random.uniform(x_min, x_max, num_points)
y_random = np.random.uniform(y_min, y_max, num_points)

# Evaluate the function at the random points
function_values = f(x_random, y_random)

# Compute the average value of the function
average_value = np.mean(function_values)

# Compute the area of the region R
area_R = (x_max - x_min) * (y_max - y_min)

# Estimate the integral
integral_estimate = average_value * area_R

# Print the result
print(f"Estimated integral using Monte Carlo integration with N = {num_points}: {integral_estimate}")

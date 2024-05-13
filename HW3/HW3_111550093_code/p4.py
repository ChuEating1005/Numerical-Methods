import numpy as np
from scipy.interpolate import RectBivariateSpline

# Define the grid points and their corresponding z values from the problem statement
x = np.array([1.3, 2.5, 3.1, 4.7, 5.5])
y = np.array([0.2, 0.4, 0.5, 0.7, 0.9])
z = np.array([
    [2.521, 2.792, 2.949, 3.314, 3.760],
    [3.721, 3.992, 4.149, 4.514, 4.960],
    [4.321, 4.592, 4.749, 5.114, 5.560],
    [5.921, 6.192, 6.349, 6.714, 7.160],
    [6.721, 6.992, 7.149, 7.514, 7.960]
])

# Create the B-spline surface
spline = RectBivariateSpline(x, y, z)

# Interpolate to find the value at (2.8, 0.54)
z_value = spline(2.8, 0.54)

print("The interpolated value of z(2.8, 0.54) is:", z_value[0][0])

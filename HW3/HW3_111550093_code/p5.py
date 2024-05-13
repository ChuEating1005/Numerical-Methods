import numpy as np

# Define the data points
x = np.array([0.40, 1.2, 3.4, 4.1, 5.7, 7.2, 9.3])
y = np.array([0.70, 2.1, 4.0, 4.9, 6.3, 8.1, 8.9])
z = np.array([0.031, 0.933, 3.058, 3.349, 4.870, 5.757, 8.921])

# Assemble the matrix A with an additional column of ones for the intercept
A = np.vstack([x, y, np.ones(len(x))]).T

# Use least squares to solve for a, b, and c
coefficients, residuals, rank, s = np.linalg.lstsq(A, z, rcond=None)

# Coefficients are a, b, and c
a, b, c = coefficients

# Calculate the fitted z values
z_fitted = a * x + b * y + c

# Calculate the sum of squares of residuals
sum_of_squares = np.sum((z - z_fitted) ** 2)

print(f"Plane equation: z = {a:.3f}x + {b:.3f}y + {c:.3f}")
print(f"Sum of squares of deviations: {sum_of_squares:.3f}")

import numpy as np

# Data points
x = np.array([-0.2, 0.3, 0.7, -0.3, 0.1])
y = np.array([1.23, 2.34, -1.05, 6.51, -0.06])

# Function to construct divided difference table
def divided_difference(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
            
    return coef

# Function to evaluate Newton's Interpolating Polynomial
def newton_interpolate(x, coef, xi):
    n = len(x) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (xi - x[n - k]) * p
    return p

### PART A ###
table = divided_difference(x, y) # Constructing the divided difference table
print(table)

### PART B ###
coef = divided_difference(x[:3], y[:3]) # Coefficients for the first three points
interpolated_value = newton_interpolate(x[:3], coef[0], 0.4) # Interpolating f(0.4) using the first three points
print("Interpolated value of f(0.4) using first three points:", round(interpolated_value, 3))

### PART C ###
sorted_indices = np.argsort(np.abs(x - 0.4)) # Selecting the best three points for f(0.4) based on proximity
print("Indices of the best three points for f(0.4):", sorted_indices[:3])
best_points_indices = sorted_indices[:3] # Choosing three points closest to 0.4 for better accuracy

# Recalculate coefficients and interpolate using the best three points
best_coef = divided_difference(x[best_points_indices], y[best_points_indices])
print(best_coef)
best_interpolated_value = newton_interpolate(x[best_points_indices], best_coef[0], 0.4)
print("Interpolated value of f(0.4) using the best three points:", best_interpolated_value)

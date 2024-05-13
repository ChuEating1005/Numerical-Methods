import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define the piecewise function
def f(x):
    if -1 <= x < -0.5:
        return 0
    elif -0.5 <= x <= 0.5:
        return 1 - 2 * np.abs(x)
    elif 0.5 < x <= 1:
        return 0
    return 0  # Ensures f(x) is defined outside the primary interval

# Polynomial definitions based on provided expressions
def custom_spline(x):
    if x < -0.5:
        return 4 * (x + 1)**2 - 2 * (x + 1)
    elif x < 0:
        return -8 * (x + 0.5)**3 + 4 * (x + 0.5)**2 + 2 * (x + 0.5)
    elif x < 0.5:
        return 8 * x**3 - 8 * x**2 + 1
    else:
        return 4 * (x - 0.5)**2 - 2 * (x - 0.5)

# Data points (must be adjusted if you have specific points)
x_points = np.array([-1, -0.5, 0, 0.5, 1])
y_points = np.array([custom_spline(x) for x in x_points])

# Cubic spline interpolations
cs_not_a_knot = CubicSpline(x_points, y_points, bc_type='not-a-knot')
cs_natural = CubicSpline(x_points, y_points, bc_type='natural')

# Dense x array for plotting smooth curves
x_dense = np.linspace(-1, 1, 400)
y_true = np.array([f(x) for x in x_dense])
y_custom = np.array([custom_spline(x) for x in x_dense])
y_not_a_knot = cs_not_a_knot(x_dense)
y_natural = cs_natural(x_dense)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x_dense, y_true, 'm-', label='Original Function f(x)', linewidth=2, color='blue', linestyle='dashed')
plt.plot(x_dense, y_natural, 'b-', label='Natural Cubic Spline', linewidth=2, color="red")
plt.plot(x_dense, y_custom, 'k-', label='Custom Cubic Spline (Condition 3)', linewidth=2, color="green")
plt.plot(x_dense, y_not_a_knot, 'r-', label='Not-a-Knot Cubic Spline (Condition 4)', linewidth=2, color="orange")
plt.scatter(x_points, y_points, color='red', s=50, zorder=5)  # Show the points used for spline fitting
plt.title('Comparison of Spline Conditions and Original Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

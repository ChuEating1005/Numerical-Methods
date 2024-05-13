import numpy as np
import matplotlib.pyplot as plt

# Define the points
points = np.array([(0, 0), (1, 0.3), (2, 1.7), (3, 1.5)])
new_points = np.array([(0, 0), (1, -1.15), (2, 3.4), (3, 1.5)])

# Function to compute Bézier curve
def cubic_bezier(t, P):
    return (1 - t)**3 * P[0] + 3 * (1 - t)**2 * t * P[1] + 3 * (1 - t) * t**2 * P[2] + t**3 * P[3]

# Generate t values
t_values = np.linspace(0, 1, 100)

# Compute points on the Bézier curve
bezier_points = np.array([cubic_bezier(t, points) for t in t_values])
new_bezier_points = np.array([cubic_bezier(t, new_points) for t in t_values])

# Plotting the Bézier curve and the control polygon
plt.figure(figsize=(8, 4))
plt.plot(points[:, 0], points[:, 1], 'o-', label='Control Polygon (Zigzag Line)')
plt.plot(bezier_points[:, 0], bezier_points[:, 1], '-', label='Cubic Bézier Curve')
plt.title('Cubic Bézier Curve with Given Control Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(points[:, 0], points[:, 1], 'o-', label='Control Polygon (Zigzag Line)')
plt.plot(new_bezier_points[:, 0], new_bezier_points[:, 1], '-', label='New Cubic Bézier Curve')
plt.title('New Cubic Bézier Curve Passing Through Control Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

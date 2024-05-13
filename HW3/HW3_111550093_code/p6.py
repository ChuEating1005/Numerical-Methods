import numpy as np
import matplotlib.pyplot as plt

# Define the function and the approximations
x = np.linspace(-2*np.pi, 2*np.pi, 400)
true_cos = np.cos(x)
chebyshev_appox = 1.0474 - 0.8794*x**2 + 0.4211*x**4
maclaurin_appox = 1 - x**2 / 2 + x**4 / 24

# Calculate errors
error1 = chebyshev_appox - true_cos
error2 = maclaurin_appox - true_cos

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(x, error1, label='Error for Chebyshev Series')
plt.plot(x, error2, label='Error for Maclaurin Series')
plt.title('Error of cos(x) Approximations')
plt.xlabel('x')
plt.ylabel('Absolute Error')
plt.legend()
plt.grid(True)
plt.ylim(-0.5, 3.5)
plt.show()

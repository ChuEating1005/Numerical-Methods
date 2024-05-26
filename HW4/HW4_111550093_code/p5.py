import numpy as np
import scipy.integrate as spi

def f(x):
    return np.exp(x)
def g(y):
    return np.sin(2 * y)

x_min, x_max = -0.2, 1.4
y_min, y_max = 0.4, 2.6
w = [0.55555555, 0.88888889, 0.55555555]
t = [-0.77459667, 0, 0.77459667]

# Part (a) Trapezoidal rule in both directions
def trapezoidal_rule_2d(x_min, x_max, y_min, y_max, h):
    x_values = np.arange(x_min, x_max + h, h)
    fi = [f(x) for x in x_values]

    y_values = np.arange(y_min, y_max + h, h)
    gi = [g(y) for y in y_values]

    f_sum, g_sum = 0, 0

    for i in range(len(x_values) - 1):
        f_sum += fi[i] + fi[i+1]
    f_sum *= h / 2

    for j in range(len(y_values) - 1):
        g_sum += gi[j] + gi[j+1]
    
    g_sum *= h / 2
    
    return f_sum * g_sum

# Part (b) Simpson's 1/3 rule in both directions
def simpsons_rule_2d(x_min, x_max, y_min, y_max, h):
    x_values = np.arange(x_min, x_max + h, h)
    fi = [f(x) for x in x_values]
    
    y_values = np.arange(y_min, y_max + h, h)
    gi = [g(y) for y in y_values]

    f_sum, g_sum = 0, 0
    
    for i in range(0, len(x_values) - 1, 2):
        f_sum += fi[i] + 4 * fi[i+1] + fi[i+2]
    f_sum *= h / 3

    for j in range(0, len(y_values) - 1, 2):
        g_sum += gi[j] + 4 * gi[j+1] + gi[j+2]
    g_sum *= h / 3

    return f_sum * g_sum

# Part (c) Gaussian Quadrature in both directions
def gaussian_quadrature_2d(x_min, x_max, y_min, y_max):
    f_sum, g_sum = 0, 0
    
    for i in range(len(w)):
        f_sum += w[i] * f((x_max - x_min) * t[i] / 2 + (x_max + x_min) / 2)
        g_sum += w[i] * g((y_max - y_min) * t[i] / 2 + (y_max + y_min) / 2)

    f_sum *= (x_max - x_min) / 2
    g_sum *= (y_max - y_min) / 2

    return f_sum * g_sum


h = 0.1

integral_trap = trapezoidal_rule_2d(x_min, x_max, y_min, y_max, h)
integral_simpson = simpsons_rule_2d(x_min, x_max, y_min, y_max, h)
integral_gauss = gaussian_quadrature_2d(x_min, x_max, y_min, y_max)

print("Trapezoidal Rule:", integral_trap)
print("Simpson's 1/3 Rule:", integral_simpson)
print("Gaussian Quadrature:", integral_gauss)

import numpy as np

def Newton_method(x, f, f_prime, tol = 10e-9):
    while(abs(f(x)) > tol):
        x = x - f(x) / f_prime(x)
    return x

f = lambda x: x**2 + np.cos(x)**4 - x - 2
f_prime = lambda x: 2 * x - 3 * np.cos(x)**3 * np.sin(x) - 1
root = Newton_method(0, f, f_prime)
print(f"root is at x = {round(root, 5)}")
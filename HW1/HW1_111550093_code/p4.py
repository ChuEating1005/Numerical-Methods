import cmath
import numpy as np

def mullers_method(f, x0, x1, x2, tol=1e-5, max_iterations=100):
    h1 = x1 - x0
    h2 = x2 - x1
    delta1 = (f(x1) - f(x0)) / h1
    delta2 = (f(x2) - f(x1)) / h2
    d = (delta2 - delta1) / (h2 + h1)
    i = 0

    while i <= max_iterations:
        b = delta2 + h2 * d
        D = cmath.sqrt(b ** 2 - 4 * f(x2) * d)
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2 * f(x2) / E
        x3 = x2 + h
        if abs(h) < tol:
            return x3
        x0, x1, x2 = x1, x2, x3
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        i += 1
    raise ValueError(f"The method did not converge after {max_iterations} iterations.")

def fa(x):
    return 4*x**3 - 3*x**2 + 2*x - 1

def fb(x):
    return x**2 + np.exp(x) - 5

x0, x1, x2 = 0, 0.5, 1
root_a = mullers_method(fa, x0, x1, x2).real

x0, x1, x2 = -3, -2, -1
root_b1 = mullers_method(fb, x0, x1, x2).real

x0, x1, x2 = 0, 1, 2
root_b2 = mullers_method(fb, x0, x1, x2).real

print(f"Root in problem a is at x = {round(root_a, 5)}")
print(f"Root in problem b is at x = {round(root_b1, 5)} and x = {round(root_b2, 5)}")
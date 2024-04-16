import cmath
import numpy as np

def fixed_point_method(x, g, tol=1e-9):
    while(abs(g(x) - x) > tol):
        x = g(x)
    return x

def g_pos(x):
    return cmath.sqrt(np.exp(x) / 2)

def g_neg(x):
    return -cmath.sqrt(np.exp(x) / 2)

def g_c(x):
    return cmath.log(2) + 2 * np.log(x)

root_a1 = fixed_point_method(0, g_pos).real
root_a2 = fixed_point_method(0, g_neg).real

root_b1 = fixed_point_method(2.5, g_pos).real
root_b2 = fixed_point_method(2.5, g_neg).real
root_b3 = fixed_point_method(2.7, g_pos).real
root_b4 = fixed_point_method(2.7, g_neg).real

root_c = fixed_point_method(2.5, g_c).real

print(f"Problem A:\n root near 1.5: x = {round(root_a1, 5)},\n root near -0.5: x = {round(root_a2, 5)}")
print(f"\nProblem B:\n x0 = 2.5 postive root: x = {round(root_b1, 5)}, negative root: {round(root_b2, 5)}")
print(f" x0 = 2.7 postive root: x = {round(root_b3, 5)}, negative root: {round(root_b4, 5)}")
print(f"\nProblem C:\n root at x = {round(root_c, 5)}")
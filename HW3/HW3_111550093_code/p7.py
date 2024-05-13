from sympy import symbols, integrate, cos, sin, pi, N

# Define variables
x, n = symbols('x n', real=True)

# Function definition
f = x**2 - 1

# Period
P = 3

# Define the integrals for coefficients
a_0 = (2/P) * integrate(f, (x, -1, 2))
a_n_expr = (2/P) * integrate(f * cos(2 * pi * n * x / P), (x, -1, 2))
b_n_expr = (2/P) * integrate(f * sin(2 * pi * n * x / P), (x, -1, 2))

# Evaluate the integrals for n = 1 to 4
print("a_0 =", N(a_0))

for ni in range(1, 5):
    a_n = N(a_n_expr.subs(n, ni))
    b_n = N(b_n_expr.subs(n, ni))
    print(f"a_{ni} =", round(a_n,4))
    print(f"b_{ni} =", round(b_n,4))

print("a_n =", a_n_expr.simplify())
print("b_n =", b_n_expr.simplify())
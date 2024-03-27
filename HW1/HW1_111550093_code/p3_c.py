import numpy as np

def f(x):
    return pow((x - 2),3) * pow((x - 4), 2)

def bisection(f, a, b, tol, cnt): 
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m the midpoint 
    # between a and b Recursive implementation
    
    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return bisection(f, m, b, tol, cnt+1)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return bisection(f, a, m, tol, cnt+1)
    
def secant(f, x0, x1, e):
    cnt = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0)) 
        x0 = x1
        x1 = x2
        cnt = cnt + 1 
        condition = abs(f(x2)) > e
    return x2

def falsePosition(f, x0, x1 ,e):
    cnt = 1
    condition = True
    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        cnt = cnt + 1
        condition = abs(f(x2)) > e
    return x2

a, b = 1, 5

root_1 = bisection(f, a, b, 10e-9, 0)
root_2 = secant(f, a, b, 10e-9)
root_3 = falsePosition(f, a, b, 10e-9)

print(f"root get by bisection: {root_1}")
print(f"root get by secant method: {root_2}")
print(f"root get by false position: {root_3}")

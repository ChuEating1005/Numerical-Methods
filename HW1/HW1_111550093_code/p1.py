import numpy as np
import math

def f(x):
    # the function given by problem 1
    return x * math.sin((x - 2) / (x - 1))

def find_intervals(f, a, b, steps):
    # divide interval [a,b] into #steps pieces, check whether each interval bracket the root
    x_values = np.linspace(a, b, steps)
    y_values = [f(x) for x in x_values]
    intervals = []
    for i in range(steps - 1):
        if y_values[i] * y_values[i + 1] < 0:
            intervals.append((round(x_values[i],5), round(x_values[i + 1],5)))
    return intervals

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
        return m, cnt
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return bisection(f, m, b, tol, cnt+1)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return bisection(f, a, m, tol, cnt+1)

# Find intervals around 0.95 where the function changes sign
intervals = find_intervals(f, 0.8, 0.98, 1000)
roots, iterations = [], []
for a, b in intervals:
    root, cnt = bisection(f, a, b, 10e-9, 0) 
    roots.append(root)
    iterations.append(cnt)
distance = list(enumerate([abs(root - 0.95) for root in roots]))
distance_sorted = sorted(distance, key=lambda x:x[1])

count = 0
for i, j in distance_sorted:
    count += 1
    if(count > 4):
        break
    print(f"{count} nearest root to x = 0.95 is at x = {round(roots[i],5)}, distance to 0.95 is {round(j,5)}, iteration times = {iterations[i]}")
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

def secant(f, x0, x1, e, N):
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
        
        if cnt > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    return x2, cnt

# Find intervals around 0.95 where the function changes sign
intervals = find_intervals(f, 0.8, 0.98, 1000)
roots, iterations = [], []
for a, b in intervals:
    root, cnt = secant(f, a, b, 10e-9, 100) 
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
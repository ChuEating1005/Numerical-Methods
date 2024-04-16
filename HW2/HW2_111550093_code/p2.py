import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 3

def Part_A(A, b):
    n = len(A)
    x = np.zeros(n)

    for i in range(n):
        for j in range(i + 1, n): 
            mul = - Decimal(A[j][i] / A[i][i])
            A[j] = [Decimal(a) + Decimal(mul) * Decimal(b) for a, b in zip(A[j], A[i])]
            b[j] += Decimal(mul) * Decimal(b[i])
    
    # back substitution
    for i in range(n - 1, -1, -1):
        x[i] = Decimal(b[i])
        for j in range(i+1, n):
            x[i] = Decimal(x[i]) - Decimal(x[j]) * A[i][j]
        x[i] = Decimal(x[i]) / A[i][i]
    
    print(f"Part A solution: {x}")

def Part_B(A, b):
    n = len(A)
    x = np.zeros(n)

    for i in range(n):
        pivot = i + np.argmax(np.abs(A[i:, i]))
        A[[i, pivot]] = A[[pivot, i]]
        b[i], b[pivot] = b[pivot], b[i]
        
        for j in range(i + 1, n): 
            mul = - Decimal(A[j][i] / A[i][i])
            A[j] = [Decimal(a) + Decimal(mul) * Decimal(b) for a, b in zip(A[j], A[i])]
            b[j] += Decimal(mul) * Decimal(b[i])
    
    # back substitution
    for i in range(n - 1, -1, -1):
        x[i] = Decimal(b[i])
        for j in range(i+1, n):
            x[i] = Decimal(x[i]) - Decimal(x[j]) * A[i][j]
        x[i] = Decimal(x[i]) / A[i][i]
    
    print(f"Part B solution: {x}")

def Part_C(A, b, s):
    n = len(A)
    x = np.zeros(n)

    for i in range(n):
        pivot, mag_max = i, np.abs(A[i, i]) / s[i]
        for j in range(i + 1, n):
            if (np.abs(A[j, i] / s[j]) > mag_max):
                pivot, mag_max = j, np.abs(A[j, i]) / s[j]
        A[[i, pivot]] = A[[pivot, i]]
        b[i], b[pivot] = b[pivot], b[i]
        
        for j in range(i + 1, n): 
            mul = - Decimal(A[j][i] / A[i][i])
            A[j] = [Decimal(a) + Decimal(mul) * Decimal(b) for a, b in zip(A[j], A[i])]
            b[j] += Decimal(mul) * Decimal(b[i])
    
    # back substitution
    for i in range(n - 1, -1, -1):
        x[i] = Decimal(b[i])
        for j in range(i+1, n):
            x[i] = Decimal(x[i]) - Decimal(x[j]) * A[i][j]
        x[i] = Decimal(x[i]) / A[i][i]
    
    print(f"Part C solution: {x}")

A = np.array([[Decimal(0.1), Decimal(51.7)], [Decimal(5.1), Decimal(-7.3)]])
b = np.array([Decimal(104), Decimal(16)])
Part_A(A, b)


A = np.array([[Decimal(0.1), Decimal(51.7)], [Decimal(5.1), Decimal(-7.3)]])
b = np.array([Decimal(104), Decimal(16)])
Part_B(A, b)

A = np.array([[Decimal(0.1), Decimal(51.7)], [Decimal(5.1), Decimal(-7.3)]])
b = np.array([Decimal(104), Decimal(16)])
s = np.array([Decimal(50), Decimal(5)])
Part_C(A, b, s)

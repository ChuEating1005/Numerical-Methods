import numpy as np

def Gaussian_Elimination(A, b):
    row_interchange = 0
    n = len(A)
    x = np.zeros(n)

    for i in range(n):
        # Partial pivoting
        pivot = i + np.argmax(np.abs(A[i:, i]))
        if (pivot != i): # Need row interchange
            row_interchange += 1
            A[[i, pivot]] = A[[pivot, i]]
            b[i], b[pivot] = b[pivot], b[i]

        # Gaussian Elimination
        for j in range(i + 1, n): # iterate each row between (i, m)
            mul = -A[j][i] / A[i][i]
            A[j] = [a + mul * b for a, b in zip(A[j], A[i])]
            b[j]+= mul * b[i] 
    
    # back substitution
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]
        x[i] = round(x[i], 3)
    
    print(f"Solution: {x}")
    print(f"Number of row interchange: {row_interchange}")

A = np.array([[3, 1, -4], [-2, 3, 1], [2, 0, 5]])
b = np.array([7, -5, 10])


Gaussian_Elimination(A, b)
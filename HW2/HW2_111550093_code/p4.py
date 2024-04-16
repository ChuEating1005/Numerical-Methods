import numpy as np

def Jocobi_Method(A, b, TOL):
    n = len(A)
    # Check for diagonally dominant 
    for i in range(n):
        d = np.argmax(A[i, 0:])
        A[[i, d]] = A[[d, i]]
        b[i], b[d] = b[d], b[i]

    x = np.zeros(n)
    diff = 1
    cnt = 0
    while (diff > TOL):
        cnt += 1
        x_prev = np.copy(x)
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i][0:], x_prev[0:]) + A[i][i] * x_prev[i]) / A[i, i]
        diff = np.sum(np.abs(x - x_prev))
    print(f"Solution: {x}\nIteration times: {cnt}")

A = np.array([[7, -3, 4], [-3, 2, 6], [2, 5, 3]])
b = np.array([6, 2, -5])

Jocobi_Method(A, b, 1e-5)
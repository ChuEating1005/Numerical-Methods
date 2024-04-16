import numpy as np

def LU_factorization(A):
    n = len(A)
    L = np.eye(n) * 2
    U = np.zeros((n, n))
    
    for j in range(n):
        U[0][j] = A[0][j] / 2 
        for i in range(1, j + 1):
            sum_u = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = (A[i][j] - sum_u) / 2
        for i in range(j, n):
            sum_l = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - sum_l) / U[j][j]

    return L, U

A = np.array([[2, -1, 3, 2], [2, 2, 0, 4], [1, 1, -2, 2], [1, 3, 4, -1]])

L, U = LU_factorization(A)

print("L:")
print(L)
print("U:")
print(U)
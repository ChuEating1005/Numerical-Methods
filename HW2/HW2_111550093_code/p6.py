import numpy as np

def Jocobi_Method(A, b, x, TOL):
    n = len(A)
    # Check for diagonally dominant 
    for i in range(n):
        d = np.argmax(A[i, 0:])
        A[[i, d]] = A[[d, i]]
        b[i], b[d] = b[d], b[i]

    diff = 1
    cnt = 0
    while (diff > TOL and cnt < 1e5):
        cnt += 1
        x_prev = np.copy(x)
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i][0:], x_prev[0:]) + A[i][i] * x_prev[i]) / A[i, i]
        diff = np.sum(np.abs(x - x_prev))
    if (cnt >= 1e5):
        print("solution diverge")
    else:
        print(f"solution: {x}")

def GaussSeidel_Method(A, b, x, TOL):
    n = len(A)
    # Check for diagonally dominant 
    for i in range(n):
        d = np.argmax(A[i, 0:])
        A[[i, d]] = A[[d, i]]
        b[i], b[d] = b[d], b[i]

    diff = 1
    cnt = 0
    while (diff > TOL and cnt < 1e5):
        cnt += 1
        x_prev = np.copy(x)
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i][0:], x[0:]) + A[i][i] * x[i]) / A[i, i]
        diff = np.sum(np.abs(x - x_prev))
    print(f"solution: {x}")


starting_vectors =  [[1, 1], [1, -1], [-1, 1], [2, 5], [5, 2]]

# Part A
print("\nPart A, Jocobi Method:")
for x in starting_vectors:
    print(f"\nStarting vector: {x}")
    A = np.array([[2, -2], [-2, 2]])
    b = np.array([0, 0])
    Jocobi_Method(A, b, x.copy(), 1e-5)

print("\nPart B:, Gauss-Seidel Method")
for x in starting_vectors:
    print(f"\nStarting vector: {x}")
    A = np.array([[2, -2], [-2, 2]])
    b = np.array([0, 0])
    GaussSeidel_Method(A, b, x.copy(), 1e-5)

# Part C
print("\nPart C, Jocobi Method:")
for x in starting_vectors:
    print(f"\nStarting vector: {x}")
    A = np.array([[2, -1.99], [-1.99, 2]])
    b = np.array([0, 0])
    Jocobi_Method(A, b, x.copy(), 1e-9)

print("\nPart C:, Gauss-Seidel Method")
for x in starting_vectors:
    print(f"\nStarting vector: {x}")
    A = np.array([[2, -1.99], [-1.99, 2]])
    b = np.array([0, 0])
    GaussSeidel_Method(A, b, x.copy(), 1e-9)
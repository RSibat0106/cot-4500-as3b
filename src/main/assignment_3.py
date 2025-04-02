import math

# ---------- Question 1: Gaussian Elimination & Backward Substitution ----------
def gaussian_elimination(A, b):
    n = len(A)
    # Forward elimination
    for k in range(n):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        value = (b[i] - s) / A[i][i]
        # If it's very close to an integer, round it
        if abs(value - round(value)) < 1e-9:
            x[i] = int(round(value))
        else:
            x[i] = value
    return x

A1 = [
    [2, -1, 1],
    [1, 3, 1],
    [-1, 5, 4]
]
b1 = [6, 0, -3]
sol1 = gaussian_elimination([row[:] for row in A1], b1[:])

print(sol1)
print()


# ---------- Question 2: LU Factorization + Determinant ----------
def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[float(A[i][j]) for j in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1.0
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U

def determinant_from_U(U):
    det = 1.0
    for i in range(len(U)):
        det *= U[i][i]
    return det

A2 = [
    [1, 1, 0, 3],
    [2, 1, -1, 1],
    [3, -1, -1, 2],
    [-1, 2, 3, -1]
]
L, U = lu_factorization([row[:] for row in A2])
det_A2 = determinant_from_U(U)

print(det_A2)
print()
# L matrix
for row in L:
    print(row)
print()

# U matrix
for row in U:
    print(row)
print()


# ---------- Question 3: Diagonal Dominance Check ----------
def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        off_diag_sum = sum(abs(A[i][j]) for j in range(len(A[i])) if j != i)
        if diag < off_diag_sum:
            return False
    return True

A3 = [
    [9, 0, 5, 2, 1],
    [3, 9, 1, 2, 1],
    [0, 1, 7, 2, 3],
    [4, 2, 3, 12, 2],
    [3, 2, 4, 0, 8]
]

if (is_diagonally_dominant(A3) == True):
    print("The matrix is diagonally dominant")
else:
    print("The matrix is not diagonally dominant")


# ---------- Question 4: Positive Definiteness Check ----------
def is_symmetric(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

def cholesky_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_ = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - sum_
                if val <= 0:
                    return None  # Not positive definite
                L[i][j] = math.sqrt(val)
            else:
                if L[j][j] == 0:
                    return None
                L[i][j] = (A[i][j] - sum_) / L[j][j]
    return L

A4 = [
    [2, 2, 1],
    [2, 3, 0],
    [1, 0, 2]
]

is_pd = is_symmetric(A4) and (cholesky_decomposition(A4) is not None)

if (is_pd == True):
    print("The matrix is positive definite")
else:
    print("The matrix is not positive definite")

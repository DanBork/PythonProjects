# Daniel Borkowy - Matrix Multiplication
# 26.11.2024

import numpy as np


def matrix_multiplication(A, B):
    columns = len(B[0])
    rows = len(A)
    if len(A[0]) == len(B):     # Verifying if matrices have correct dimensions for multiplication
        C = [[0 for _ in range(columns)] for _ in range(rows)]  # Initialising result matrix
        for i in range(rows):                           #
            for j in range(columns):                    # Iterating and multiplying
                for k in range(len(B)):                 #
                    C[i][j] += A[i][k]*B[k][j]          #

        return C
    else:
        print("Incorrect dimensions for matrix multiplication")
        return


A = [[55, -7, 23], [46, -25, 6], [-7, 8, 9]]                # Example Matrices
B = [[5, 0, 0, 20], [6, 97, -3, 20], [42, 55, -9, 1]]


C = matrix_multiplication(A, B)
C_test = np.matmul(A, B)
print("Result of multiplication:")
for n in range(len(C)):
    print(C[n])
print("\nMultiplication using NumPy:\n", C_test)    # Visual Confirmation of result

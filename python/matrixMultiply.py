# Multipy some hard-coded matrices. Used for a problem set in the class 3D Spacial Modeling and Computing
import numpy as np
import sympy as sp

def problem_2():
    A = np.array([[2, 5], [1, 9]])
    B = np.array([[6, 2], [2, 8]])
    C = np.array([[0, 1], [4, 7]])

    ABCA = A @ B @ C @ A
    BACA = B @ A @ C @ A
    CABA = C @ A @ B @ A
    CBAA = C @ B @ A @ A
    AABC = A @ A @ B @ C
    ABAC = A @ B @ A @ C
    ACAB = A @ C @ A @ B
    ACBA = A @ C @ B @ A

    res = ABCA - BACA - CABA + CBAA - AABC + ABAC + ACAB - ACBA
    print(res)

def problem_6():
    T1 = np.array([[0,1,-2],[-1,0,1],[0,0,1]])
    T2 = np.array([[0,1,3],[-1,0,4],[0,0,1]])
    print(T1 @ T2)

def se_log_translations():
    # Define the symbols
    a, b, c, q, p = sp.symbols('a1 a2 a3 q2 p2')

    # Create two 3x3 matrices with symbols
    A = sp.Matrix([
        [0, -c, b],
        [c, 0, -a],
        [-b, a, 0]
    ])

    # Multiply the matrices
    product1 = p * A * A
    product2 = q * A

    p2 = A * A
    p3 = A * p2
    p4 = A * p3

    print(sp.pretty(p2))
    print(sp.pretty(p3))
    print(sp.pretty(p4))


    print(sp.pretty(product1))
    print(sp.pretty(product2))
    result = sp.eye(3) + product1 + product2
    print(sp.pretty(result))
    inv_result = result.inv()
    print(sp.pretty(inv_result))

se_log_translations()
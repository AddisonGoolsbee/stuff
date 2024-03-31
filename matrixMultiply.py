# Multipy some hard-coded matrices. Used for a problem set in the class 3D Spacial Modeling and Computing
import numpy as np

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

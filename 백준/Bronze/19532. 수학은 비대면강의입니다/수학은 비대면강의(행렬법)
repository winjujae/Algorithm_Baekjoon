#19532번 수학은비대면강의입니다(행렬)
import numpy as np
a, b, c, d, e, f = map(int, input().split())

A = np.array([[a, b], [d, e]])
B = np.array([c, f])

det_A = np.linalg.det(A)

if det_A == 0:
    print("inf or no ans")
else:
    A_inv = np.linalg.inv(A)
    X = np.dot(A_inv, B)
    print(round(X[0]), round(X[1]))

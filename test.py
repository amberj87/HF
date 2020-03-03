import numpy as np

A=np.zeros([5,5])
B=np.zeros([5,5])

C=A+B+1
C=C.dot(C)
print(C)

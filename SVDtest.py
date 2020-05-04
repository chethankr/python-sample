import numpy as np
import numpy.linalg as la

from math import *

inV = [2,4,6,8,9,3]
inV = np.array(inV)[np.newaxis]
z = np.matmul(inV.T,inV)
print(z)
print('******************************************')

#SVD
U,D,V = la.svd(z)
print(U)
print(D)
print(V)

print('**********identity ?????********************************')
ident = np.matmul(U,U.T)
print(ident)

print('**********U.vT ?????********************************')
UvT = np.matmul(U[0],V.T)
print(UvT)
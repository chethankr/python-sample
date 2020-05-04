import numpy as np
import numpy.linalg as la

from math import *

input = [1+2j,56+3j,78+4j,23+5j,56+7j,89+8j,12+9j,23+1j]

print(type(input))


x = np.array(input)[np.newaxis]
#print(x)
#print(x.T)
CR = np.matmul(x.T,x)
#print(CR)

#print('******************************************')


#SVD
U,D,V = la.svd(CR)
#print(D)
#print('******************************************')
#print(V)

print('*******************Exy***********************')
ExyV = V[0]


print('******************************************')
Exy1 = ExyV[0:7]
Exy2 = ExyV[1:8]



'''
print(Exy1)
print('******************************************')
print(Exy2)
print('******************************************')
'''
'''
# get 2 * 7 matrix.
Exyz = np.concatenate((Exy1, Exy2))
#print(Exyz)
Exyz = Exyz.reshape(7,2)
#print('******************************************')
#print(Exyz.shape)
'''


ExyV1 = V[1]
vecxy1 = ExyV1[0:7]
vecxy2 = ExyV1[1:8]

print(vecxy1)
print('******************************************')
print(vecxy2)
print('******************************************')


args = Exy1, Exy2,vecxy1,vecxy2
Exyz = np.concatenate(args)
#print(Exyz)
Exyz = Exyz.reshape(7,4)
print('******************************************')
print(Exyz.shape)
print(Exyz)


#autocorrelation
E_xys = np.matmul(Exyz.T,Exyz)
print('********E_xys**********************************')
print(E_xys)



#SVD

U,EVA_xys,EV_xys =la.svd(E_xys);
print('****************EV_xys**************************')
print(EV_xys)



'''
#decomposition of eigenvectors
Gx = EV_xys[0][1]
Gy = EV_xys[1][1]



'''
# try thi first 2 vec.
argsx = [EV_xys[0][2],EV_xys[0][3]],[EV_xys[1][2],EV_xys[1][3]]
argsv = [EV_xys[2][2],EV_xys[2][3]],[EV_xys[2][2],EV_xys[2][3]]
MGx = np.array(argsx)
MGy = np.array(argsv)



MGx = MGx.reshape(2,2)
#print('shape' , MGx.shape())
U,SMGx,V = la.svd(MGx)

MGy = MGy.reshape(2,2)
U,SMGy,V = la.svd(MGy)

print('SMGx, SMGy',SMGx , SMGy)

Gx= SMGx[0]
Gy= SMGy[0]

print('Gx, Gy',Gx , Gy)
print('******************************************')





print('Gx, Gy',Gx , Gy)

#calculation of  Psi
EGS = Psi = -Gx/Gy;
'''
print(Psi)
print('******************************************')

'''



#DOA estimates
ephi = atan2(EGS.imag, EGS.real);
print('ephi' , ephi)
angle =  asin( ephi / (2*pi*0.5) );
print('angle' , angle *180 / pi)
print('**************END****************************')
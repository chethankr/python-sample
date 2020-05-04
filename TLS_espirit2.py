import numpy as np
import numpy.linalg as la
import scipy.linalg as sla

from math import *

input = [
        [1.6377e+004 - 1.7277e+003j , 1.6423e+004 - 1.9331e+003j , 1.5938e+004 - 1.6482e+003j , 1.5763e+004 - 1.7500e+003j,  1.5824e+004 - 1.9713e+003j, 1.5904e+004 - 1.9104e+003j , 1.5832e+004 - 1.5149e+003j , 1.5949e+004 - 1.6583e+003j],
        [1.6155e+004 - 1.7812e+003j , 1.6463e+004 - 1.6592e+003j,  1.6510e+004 - 1.5006e+003j , 1.6346e+004 - 1.7219e+003j,  1.6233e+004 - 1.4808e+003j ,1.6052e+004 - 1.6222e+003j, 1.5476e+004 - 1.3929e+003j, 1.6028e+004 - 1.3516e+003j],
        [1.5963e+004 - 1.7869e+003j,  1.6285e+004 - 1.4558e+003j , 1.6337e+004 - 1.8269e+003j,  1.5997e+004 - 1.7289e+003j,  1.6133e+004 - 1.4700e+003j, 1.6487e+004 - 1.2785e+003j,  1.5746e+004 - 1.7482e+003j,  1.5512e+004 - 1.4252e+003j],
        [1.6074e+004 - 2.1666e+003j,  1.5894e+004 - 1.5283e+003j,  1.5924e+004 - 1.3183e+003j,  1.5801e+004 - 1.8131e+003j,  1.6165e+004 - 1.3294e+003j, 1.6103e+004 - 1.4241e+003j,  1.6083e+004 - 1.7959e+003j,  1.5814e+004 - 1.4250e+003j],
        [.6001e+004 - 2.2518e+003j,  1.6080e+004 - 1.8425e+003j,  1.6368e+004 - 1.7414e+003j,  1.6593e+004 - 1.4751e+003j,  1.6678e+004 - 1.4704e+003j ,1.6323e+004 - 1.6955e+003j , 1.6020e+004 - 1.7735e+003j,  1.6016e+004 - 1.3546e+003j],
        [1.6145e+004 - 1.9429e+003j,  1.6636e+004 - 1.5080e+003j,  1.6452e+004 - 1.1838e+003j,  1.6057e+004 - 1.4739e+003j , 1.6027e+004 - 1.3440e+003j ,1.5918e+004 - 1.2179e+003j , 1.5649e+004 - 1.5347e+003j , 1.6173e+004 - 1.0870e+003j],
        [1.6044e+004 - 1.5566e+003j , 1.6207e+004 - 1.8451e+003j,  1.6060e+004 - 1.3686e+003j , 1.5835e+004 - 1.5833e+003j , 1.6375e+004 - 1.8806e+003j ,1.6117e+004 - 1.6093e+003j , 1.5853e+004 - 1.6248e+003j,  1.6246e+004 - 1.6051e+003j],
        [1.6120e+004 - 1.7039e+003j,  1.6006e+004 - 1.8593e+003j,  1.5985e+004 - 1.2376e+003j,  1.6367e+004 - 2.0155e+003j , 1.6106e+004 - 1.2029e+003j, 1.6080e+004 - 1.6863e+003j , 1.6014e+004 - 1.7122e+003j , 1.6090e+004 - 1.1754e+003j]
        ]


x = np.array( input )

print(x.shape)
CR = np.matmul(x.T,x)
#print(CR)
#print('******************************************')


print('********************numpy D**********************')
#SVD
U,D,V = la.svd(CR)
print(D)

#print(V)

'''
print('********************scipy D**********************')
# scipy SVD
U,D, V = sla.svd(CR)
print(D)
'''


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
argsv = [EV_xys[2][2],EV_xys[2][3]],[EV_xys[3][2],EV_xys[3][3]]
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
from typing import Any, Union

import numpy as np
import numpy.linalg as la

import pandas as pd

from skimage.transform import resize
import matplotlib.pyplot as plt



def pca(X):
  # Principal Component Analysis
  # input: X, matrix with training data as flattened arrays in rows
  # return: projection matrix (with important dimensions first),
  # variance and mean

  #get dimensions
  num_data,dim = X.shape

  plt.plot(X)
  plt.title("only X")
  plt.show()

  #center data
  mean_X = X.mean(axis=0)
  print('mean_X' , mean_X)
  print('=====================================================\n')
  for i in range(num_data):
      X[i] -= mean_X

  plt.plot(X)
  plt.title("Mean X")
  plt.show()


  if dim  > 100:
      print('PCA - compact trick used')
      M = np.dot(X,X.T) #covariance matrix
      e,EV = la.eigh(M) #eigenvalues and eigenvectors
      tmp = np.dot(X.T,EV).T #this is the compact trick
      V = tmp[::-1] #reverse since last eigenvectors are the ones we want
      S = np.sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
  else:
      print('PCA - SVD used')
      U,S,V = la.svd(X)
      V = V[:num_data] #only makes sense to return the first num_data

  #return the projection matrix, the variance and the mean
  return V,S,mean_X
   

def convstr(m,n):
    T = [m, n]
    # print(type(T))
    str = ''.join(T)
    # print(str)
    v1 = str.replace(" ", "")
    # print(v1)
    val = int(v1, 16)
    #print(val)
    return val



# reading csv file
df = pd.read_csv("APTIV2.csv")

#print(df.head())

List = []
List2 = []
cnt = 0;

for x,y in enumerate(df.values ):
    #print(x)

    List = y
    v1 = convstr(List[0], List[1])
    v2 = convstr(List[2], List[3])
    v3 = convstr(List[4] , List[5])
    v4 = convstr(List[6] , List[7])
    v5 = convstr(List[8] , List[9])
    v6 = convstr(List[10] , List[11])
    #print(v1,v2,v3,v4,v5,v6)
    L = [v1, v2, v3, v4, v5, v6]
    #print(L)
    List2.append(L)

print('list -----------created')

x = np.array(List2)[np.newaxis]
print(x.shape)
print(x.size)

x= x.reshape(x.size , 1 )
print('x - reshaped' , x.shape)
#print(x)


x_rez = resize(x, (100 , 100))
x_rez= x_rez.reshape(x_rez.size,1)
print('x_rez - reshaped' , x_rez.shape)

x_rez = x_rez.astype('float32')
Vx,Sx,mn_X = pca(x_rez)
print(Vx)

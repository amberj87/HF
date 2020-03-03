import numpy as np
import math
from file_read import file_read

def compute_S_neg_half(S,n):
  eig_vec,eig_val=np.linalg.eig(S)
  for i in range(n):
    if(S[i][i]>0):
      S[i][i]=1.0/math.sqrt(S[i][i])
  S_neg_half=np.zeros([n,n])
  S_neg_half=np.multiply(eig_vec,S)
  S_neg_half=np.multiply(eig_vec.transpose(),S_neg_half)
  return(S_neg_half)

n=7
S=file_read('S.dat',n)
#print(S)
S_neg_half=compute_S_neg_half(S,n)
print(S_neg_half)

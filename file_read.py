import numpy as np 

def file_read(file_name,nbasis):
  input_file=open(file_name)   #open the file
  file_content=input_file.readlines()# read the content
  input_file.close()            # close the file

  temp_mat=[]
  A=np.zeros([nbasis,nbasis])
  for line in file_content:
     V_line=line.rstrip()
     V_line=V_line.split()
     i=int(V_line[0])-1
     j=int(V_line[1])-1
     A[i][j]=float(V_line[2])
     A[j][i]=float(V_line[2])
     #temp_mat.append(V_line.split())

  #ind=0
  #for i in range(nbasis):
  #  for j in range(i+1):
  #    A[i][j]=temp_mat[ind][2]
  #    A[j][i]=A[i][j]
  #    ind=ind+1
  return A

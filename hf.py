#This a program to calculate the Hatree-Fock energy of a closed shell molecule
#Read the geometry
from no_of_el import no_of_e
from find_distance import find_distance
from file_read import file_read
from guess_P import guess_P
#from compute_F_mat import compute_F_mat
#from compute_F_mat_prime import compute_F_mat_prime
from compute_S_neg_half import compute_S_neg_half
import numpy as np

input_file=open('geom.dat')   #open the file

file_content=input_file.readlines()# read the content

input_file.close()            # close the file

#print(file_content)


# store the input in list
temp_geom=[]
for line in file_content:
  v_line=line.rstrip()
  if len(v_line)>0:
    temp_geom.append(v_line.split())

#no of atoms
NATOM=int(temp_geom[0][0])
print('Total no of atom '+str(NATOM))
print()
ATOM_SYMBOL=[] # this list contains the atom symbols
#ATOM_el=[] # this list contains the atom symbols
ATOM_el=np.zeros([NATOM]) # this list contains the atom symbols
for i in range(1,NATOM+1): 
  ATOM_SYMBOL.append(temp_geom[i][0])
  #ATOM_el.append(no_of_e(ATOM_SYMBOL[i-1]))
  ATOM_el[i-1]=no_of_e(ATOM_SYMBOL[i-1])

print("Symbols and the atomic number")
print(ATOM_SYMBOL)
print(ATOM_el)

coordinates=np.zeros([NATOM,3])
#coordinates=[]
for i in range(NATOM):
  #coordinates.append(temp_geom[i+1][1:3])
  coordinates[i][0:2]=temp_geom[i+1][1:3]

print()
print("coorindates of the molecules")
print(coordinates)

## calculate nuclear repulsion energy
nuclear_repulsion=0.0
for i in range(NATOM):
  for j in range(NATOM):
    if(i!=j):
      dis=find_distance(coordinates[i],coordinates[j])
      nuclear_repulsion+= ATOM_el[i]*ATOM_el[j]/dis

nuclear_repulsion=nuclear_repulsion/2.0
print()
print("nuclear_repulsion energy in a.u.")
print(nuclear_repulsion)
print()

#-----------------------------------------------------------------  
## basis set
nbasis=7

#-----------------------------------------------------------------  
#read one electron integrals
#S=np.zeros([nbasis,nbasis])
S=file_read('S.dat',nbasis)
V=file_read('V.dat',nbasis)
T=file_read('T.dat',nbasis)

H=np.zeros([nbasis,nbasis])
H=np.add(T,V)
print("H_core matrix")
print(H)
#S_neg_half=compute_S_neg_half(S,nbasis)

#-----------------------------------------------------------------  
#read two electron integrals
V_el=file_read_2el()



#-----------------------------------------------------------------  
#density_mat=guess_density_mat()
#P=guess_P(nbasis)

#tolerance=1
#error=100.0
#do while(error<tolerance)
#  F_mat=compute_F_mat()
#  F_mat_prime=compute_F_mat_prime()
#  eig_vec,eig_val=np.linalg.diag(F_mat_prime)
 

from math import sqrt
def find_distance(a,b):
  dis=0.0
  for i in range(3):
    x=float(a[i])
    y=float(b[i])
    dis+=(x-y)**2
  dis=sqrt(dis)
  #dis=dis**0.5
  return(dis)


#################################################
#O=[0.000000000000,-0.143225816552,0.000000000000]
#H=[1.638036840407,1.136548822547,-0.000000000000]
#dist=find_distance(O,H)
#print('distance_between O and H '+str(dist))

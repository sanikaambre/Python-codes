import numpy as np
a=np.array([[1,0,0,2],[0,0,3,0],[0,0,0,0],[0,2,0,0]],dtype=np.f)
print("Original Array")           
print(a)
u,s,v=np.linalg.svd(a,full_matrices=False)
q,r=np.linalg.qr(a)
print("Factor of a given array by Singular Value Decompostion ")
print("u=\n",u,"\ns=\n",s,"\nv=\n",v)

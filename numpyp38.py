import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrix")
print(p)
print(q)
result=np.outer(p,q)
print("Outer product of the said  two vectors :")
print(result)

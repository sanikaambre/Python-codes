import numpy as np
fvalues=[0,12,45.21,34,99.91,32]
F=np.array(fvalues)
print("Values in Fahreneit degrees:")
print(F)
print("Values in Centigrade degrees:")
print(np.round((5*F/9-5*32/9),2))

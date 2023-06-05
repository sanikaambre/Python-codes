import pandas as pd
import numpy as np
d={'col1':[1,4,3,4],'col2':[2,4,6,8],'col3':[1,3,5,7]}
df=pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("Value of Row 1")
print(df.iloc[0])
print("Value of Row 3")
print(df.iloc[3])

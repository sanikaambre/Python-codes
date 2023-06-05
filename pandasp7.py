import pandas as pd
import numpy as np
exam_data={'name':['Annie','Shreya','Sahil','Amisha','Riya','Aarya'],'score':[12,67,35,40,56,99],'attempts':[1,3,2,1,3,2],'qualify':['yes','no','yes','yes','no','yes']}
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,labels)
print("Original rows:")
print(df)
print("\n Append a new row:")
df.loc['k']=['Suresh',13,2,'yes']
print("Print all records after insert a new record")
print(df)
print("\n Delete the new row and display the original row")
df=df.drop('k')
print(df)


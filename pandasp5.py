import pandas as pd
import numpy as np
exam_data={'name':['Annie','Shreya','Sahil','Amisha','Riya','Aarya'],'score':[12,67,35,40,56,99],'attempts':[1,3,2,1,3,2],'qualify':['yes','no','yes','yes','no','yes']}
labels=['a','b','c','d','e','f']
df=pd.DataFrame(exam_data,labels)
print("Rows where the score is between 40 and 60(inclusive):")
print(df[df['score'].between(40,60)])

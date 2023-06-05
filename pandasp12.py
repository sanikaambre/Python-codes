import pandas as pd
df=pd.DataFrame({'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print("Original DataFrame")
print(df)
print("\n Add prefix")
print(df.add_prefix("00_"))
print("\n Add sufix:")
print(df.add_suffix("_0Y0"))

import pandas as pd

df1 = pd.read_csv("pandas-master/pokemon_data.csv")
df1 = df1.iloc[:166,0:10]
print(df1)

for i, row in df1.iterrows():
    if "Mega" in row["Name"]:
        df1 = df1.drop(index=i,axis=0)

df1["Total"] = df1.iloc[:,:10].sum(axis=1)
cols = list(df1.columns.values)
df1 = df1[cols[0:4] + [cols[-1]] + cols[4:10]]
df1t1 = df1["Type 1"]
df1t2 = df1["Type 2"]
df1 = df1.drop(columns=["Type 1","Type 2"])
df1["Type 1"] = df1t1
df1["Type 2"] = df1t2
cols1 = list(df1.columns.values)
df1 = df1[cols1[:2]+cols1[3:9]+cols1[2:3]+cols1[9:11]]
df1.loc[43,"Type 2"] = "Olcie"
df1.loc[43,"Type 1"] = "Kocham"
print(df1)
df1.to_csv("pokedata.csv",index=True)

import pandas as pd

df1 = pd.read_csv("pandas-master/pokemon_data.csv")
df1 = df1.head(166).sort_values(["Generation","#"])
# Dropping a column:
# df1 = df1.drop(columns="#")
print(df1)
# Adding columns values in every row as TOTAL:
# 1th trial xd
# for row in df1.iterrows():
#     for col in row:
#         print(col)
#
# df1["Total"] = df1.iloc[:,4:10].sum(axis=1)
# # or (probably its safer for our metadata changing during he code edition)
df1["Total"] = df1.loc[:,"HP":"Speed"].sum(axis=1)
# So... xd we pointed all rows in 4to10 column and
# used .sum method which takes axis 0 for vertical 1 - horizontal
cols = list(df1.columns.values)
df2 = df1[cols[0:3] + [cols[-1]] + cols[3:12]]
# drop(self,labels=,axis=,index=,columns=,level=,inplace=)
# df2.loc[0,"Total"] = 0

# !! Trying to remove rows with Megapoke's:
for i, row in df2.iterrows():
    if "Mega" in row["Name"]:
        df2 = df2.drop(index=i, axis=0)
        print(row["Name"], i)
# WIN!


# df3 = df2["#"].unique()
# print(df3)

# df2 = df2.reset_index(drop=True,inplace=True)
# not useful with html format because of indexing
# relevancy

print(df2)
df2.to_html("pokemon_data2.html", index=True)

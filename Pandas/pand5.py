import pandas as pd
import re
from time import sleep
# df1 = pd.read_csv("pokedata.csv")
df1 = pd.read_csv("pandas-master/pokemon_data.csv")
# df1.to_html("pokedata1.html",index=True)
# sleep(5)

# RETURN SPECIFIC DATA:
# df1 = df1.loc[0:10,["Name","Speed"]]
# print(df1)

# RETURN WITH REMOVE INDEXES:
# we can add a cond with DF.loc[(DataFrame[Header] if x)]
df1 = df1.loc[(df1['Generation'] <= 2)]
# print(df2)
# DF[H].str.contains("") with ~ as negation:
df1 = df1.loc[~(df1['Name'].str.contains("Mega"))]
df1 = df1.drop(columns=["#","Legendary"])
# ADD A COLUMN WITH .sum method
df1["Total"] = df1.loc[:,"HP":"Speed"].sum(axis=1)
# AND ARRANGE:
cols = list(df1.columns.values)
df1 = df1[[cols[0]]+cols[3:9]+[cols[-1]]+cols[1:3]+[cols[-2]]]
# pd.DataFrame.insert()

# RETURN SELECTED TYPES OF DATA WITH .str.
# df1 = df1.loc[df1["Type 1"].str.contains("fire|grass", flags=re.I,regex=True)]
# MORE SELECTING:
# df1 = df1.loc[df1["Name"].str.startswith("Pi")]

# GROUPING:
# df1 = df1.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False)
# df1 = df1.groupby(["HP"]).mean().sort_values("Total",ascending=False)
# df1 = df1.groupby("Type 1").count().sort_values("Name")


# print(ss1)


# df1.reset_index(drop=True,inplace=True)
# print(df1.index)
# df1.insert(df1.index[-1]+2,"Type 1",10,True)
df1.to_html("pokedata1.html", index=True)
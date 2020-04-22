import pandas as pd
import numpy as np

# # PANDAS ELEMENTARY:
# DATA MINING:

# Sometimes AFTER IMPORTING data to analyses we first have to
# REARRANGE IT, prepare, because of some values may be missing or
# have to be changed (i.e. inch->cm) or oppositely
# some labels are doubled and we need to remove
# or change indexes for some rows of values

# MISSING DATA: NaN
df1 = pd.read_csv("realdata/4IB.F.csv", index_col=0)[0:10]
print(df1)
# 'adding' NaN data:
# df1.iloc[len(df1.index.values)-1] = np.nan  # changing last row values
df1["Open"] = np.nan  # changing first column
df1["Avarage"] = np.nan  # adding column on the end
df1.insert(5,"Sum","Nan")
ss1 = pd.DataFrame({"A":[1,2,3]})
df2 = pd.concat([df1,ss1],axis=0)
print(df2)
df1.iloc[3,1] = np.nan
print(df1)
# ! IMPORTANT: for some reason I though that putting data column as index should let us treat is
# as a column more than index column : o what I want to say is:
# loosing some headers while saving and loading DF is not so hard to
# turn back to wanted state:
df1 = df2
df1.iloc[3,1] = np.nan
df1.iloc[4,3] = np.nan
df1.iloc[8,4] = np.nan
df1.iloc[2,5] = np.nan
print(df1)
df1.index.name = "Date"
print(df1.isnull())  # returns DF of boolean values
print(df1.isnull().sum())  # returns Series of sums of NaN's occurances in each column
print(df1.isnull().sum().sum())  # returns a num which is sum of sums of Nans of each col

print(df1.count())  # returns Series of sums of non-NaN values in each row
# print(df1.isnull().count().count())  # returns Series of sums of non-NaN values in each row
len(df1)



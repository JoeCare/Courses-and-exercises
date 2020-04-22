import pandas as pd
import numpy as np
# # PANDAS ELEMENTARY:
# # DATA FRAMES: INDEXING,
# # DATA VALUES LOOKUP WITH SCALAR AND BY SLICING,
# # BASIC CONDITIONAL SLICING,
# # COLLETING INFO ABOUT DF, EDITING HEADERS,
# # ADDING AND DELETING COLUMNS

# # DATA FRAMES:
sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
print(sales1)
df1 = pd.DataFrame({2017:sales1})
print(df1)
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df2 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})
print(df2)

# INDEXING, RETURNING DATA ABOUT DATAFRAME .columns .index .shape:
print(df2.shape)  # returns number of (rows,columns)
df2.columns = ["A","B","C"]
df2.index = ["Y","F","M","G"]
print(df2)  # indexes and columns names changed

# REINDEXING SPECIFIC COLUMNS and INDEX with .rename:
df2 = df2.rename(index={"G":"Google"},columns={"A":2017})
print(df2)
df2.rename(columns={2017:2019}, inplace=True)  # inplace attribute True indicate that
# operation is made on the original DF (without assignment like in a line above)
print(df2)

df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})  # original DF
print(df1.shape,df1.columns,df1.index)  # same operations for original DF

# RETURNING DATA VALUES for DF with .take:
sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})
print(df1[[2015,2017]].take([0,2]))  # return specified rows of two columns
# IN DATA FRAMES WE USE [] NOTATION for
# SELECTING COLUMNS (besides slicing) as we used it in SERIES to SELECT ROWS.

# IMPORTANT difference:
print(type(df1[[2015]]))  # column in double brackets is DF type
print(type(df1[2015]))  # column in single bracket is Series type

# # HEADERS:
df1.columns = ["seventeen","sixteen","fifteen"]  # change headers for str's
df1.index.name = "Ind/"  # change/add index for column header
df1.columns.name = "Year 20':" # and header for columns row; same with:
df1 = df1.rename_axis(index="Company/",columns="Two thousand-")
# so its practically the same again as with REINDEXING section above
print(df1.sixteen)  # it won't work with int's saved in str's like "16"
print(df1)
print(df1.columns.get_loc('fifteen'))  # returns 'index'(number/counter) of a column

# # SELECTING ROWS and SCALAR LOOKUP:
sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})

# SLICING DATAFRAME:
print(df1[:3:2])
# IMPORTANT: beside slicing
# DATA FRAMES USE [] notation for SELECTING COLUMNS not-ROWS, so:
# print(df1[1])  # ,
# print(df[0,1,3])  # or
# print(df1[[0,1,3]])  # returns error

# SLICING WITH .loc .iloc:
print(df1.loc[["Google","Microsoft"]])  # and:
print(df1.iloc[[3,2]])  # return the same

# IMPORTANT: basic CONDITIONAL SLICING:
df1 = pd.DataFrame({"A":sales1,"B":sales2,"C":sales3})
print(df1.A > 300)  # returns Series of boolean value for each row in selected column
print(df1[df1.A > 300])  # returns DataFrame with values of the rows
# fulfilling the condition for specified column

# SCALAR LOOKUP of values using 2 selectors;
# first is .at selector for index and column and second is ... :
print(df1.at["Google","B"])  # returns value of [row"Google,column"B"]
# .at is ok for getting or setting single value; .loc/.iloc are almost the same
print(df1.iat[3,1])  # same using default indexing

# ADD NEW COLUMN to DF:
df1 = pd.DataFrame({"A":sales1,"B":sales2,"C":sales3,"D":([80,60,150,120])})
df1.rename(columns={"D":2012,"C":2014,"B":2015,"A":2016}, inplace=True)  # has the same effect as:
# df1 = df1.rename(columns={"D":2013,"C":2014,"B":2015,"A":2016})
df1[2011] = ([70,50,90,90])  # adding specified column at the end of DF
df1.insert(3,2013,[80,110,200,220])  # adding specified at the 3th position of DF
df1[2010] = df1[2011]//2 - 5  #
print(df1)

# DELETING COLUMNS and ROWS .pop() .drop() del(DF[x]):
df2 = df1.drop("Yahoo",axis=0)  # deleting row with axis=0
df2 = df1.drop(2010,axis=1)  # to not change the original DF or:
df1.drop(2010,axis=1,inplace=True)  # directly changing DF by attribute inplace=True
# if we put it above previous line, its can't be committed; axis=1 for column, 0 for a row
df1.pop(2011)
del(df1[2012])
print(df1)

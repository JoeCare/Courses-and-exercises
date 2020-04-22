import pandas as pd
import numpy as np

# # PANDAS ELEMENTARY:
# # HIERARCHICAL INDEX, REINDEXING and MULTI-INDEXING

sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})
print(df1)
# RESETING INDEXES for default or FOR SPECIFIED COLUMN
# sometimes we may need numerical indexing
# but want to leave current indexes as a column:
df2 = df1.reset_index()
print(df2)  # original DF1 stays intact
df2.rename(columns={"index":"Old Index"},inplace=True)  # my addition for more clear column names
df2.columns.name = '#'  # also my addition; it's placed above indexes so i set '#' but it's indeed
# 'index' value of the column names row; df2.index.name would be index value for index values ; o
# SETTING SPECIFIED COLUMN AS DF INDEX
df2 = df2.set_index(2016)  # sets '2016' column rows as new indexes
# my trial:
df2 = df2.set_value(250,2017,350)  # is similar to:
df2.loc[250,[2017]] = 300
# irrelevant for the subject here.
print(df2)
df2 = df1.reindex(index=["Yahoo","F","Google","MS"])  # if new indexes are not the same as old
print(df2)
# values in all columns become Nan (wtf, qui bono?); anyway original DF... still may be intact : o
# becouse it would be awful it'd change its indexes for the same indexes? xD
# or maybe it is for easy clearing of the non-aligned rows...
# but who would remember whole list of mln indexes to put it into that method...
# i think it may be used with company of df1.index... hmmm:
df2 = df2.reindex(index=(df1.index))  # yup, it takes previous df1 indexing
print(df2)
# it can also be done to destroy DF by reindexing columns
df2 = df2.reindex(columns=[2000,2017,2011])  # leaves only values of aligned '2017' column
print(df2)
# HIERARCHICAL MULTI-INDEXING: when some more general columns are needed
df1 = pd.DataFrame({"Age":[1,3,5,7],"Year":[2000,2001,2002,2003],"Angola":[1,2,3,4],"Zambia":[
    1.2,2.2,3.2,4.2]})
print(df1)
df1 = df1.set_index(["Year","Age"])  # we have 2-leveled multi-indexed DF
print(df1)
print(type(df1.index))  # confirms MiltiIndex type
print(len(df1.index.levels))  # confirms 2 levels in levels list
# IMPORTANT: (i think) LIST OF LIST! We've got ourselves a 2-d matrix inside a DF : o wdk
# what with it
# as in the matrix we can access each lvl separately; my trial:
print(df1.index.levels[0])  # as well as each index value on indicated lvl:
print(df1.index.levels[0][0])
print(df1.iloc[[1],[0]])  # returns DF
print(df1.iloc[[0][0],[1]])  # returns particular Series;
# [[lvl0 value index][lvl1 value index],[column value index]]
# back to course:
print(df1.xs(2000))  # returns DF of lvl0, takes value of indicated lvl index
print(df1.xs(1, level= 1))  # returns DF of lvl1; like above contains also indexes of lvl not
# mentioned in method
print(df1.xs(2000,drop_level=False))  # now it mentions both lvls indexes






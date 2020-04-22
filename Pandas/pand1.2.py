import pandas as pd
# # PANDAS ELEMENTARY:
# # ADDING DFs, ADDING ROWS to DF,
# # FINDING positional indexes for INDEX AND COLUMNS,
# # MATH OPERATIONS

# ADDING DATA FRAMES:
sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})
print(df1)
sales4 = pd.Series([200,300,400,500],index=['Amazon','Ebay','Jumia','Etsy'])
sales5 = pd.Series([150,250,350,450],index=['Amazon','Ebay','Jumia','Etsy'])
sales6 = pd.Series([100,200,300,400],index=['Amazon','Ebay','Jumia','Etsy'])
df2 = pd.DataFrame({2017:sales4,2016:sales5,2015:sales6})
print(df2)

df3 = df1.append(df2)
df3 = df2.append(df1)  # gives obviously another DF
print(df3)

df4 = pd.DataFrame({2013:sales4,2014:sales5,2015:sales6})

df3 = df1.append(df4)  # returns NaN for non-aligned columns
print(df3)

# ADD NEW ROW:
df3.loc["MBI"] = [70,90,120,150,300]
print(df3)
# CHANGING CERTAIN localization on DF:
df3.loc["Microsoft",2015] = 150
print(df3)
# in a large DF it may need to indicate positional index so:
# FINDING INDEX and COLUMN:
microsoft_position = df3.index.get_loc("Microsoft")
ttfiveteen_position = df3.columns.get_loc(2015)
df3.iloc[microsoft_position,ttfiveteen_position] = 100
print(df3)

# MATH OPERATIONS:
df4 = df3 * 2  # all values raised 2 times
print(df4)
ss1 = df3.iloc[0]  # declaring Series with Yahoo row
print(ss1)
df4 = df3 - ss1  # reduces all Yahoo row non-Nan columns to 0
print(df4)
df4 = ss1 - df3  # Yahoo 0 and turns every other non-Nan values to negative
print(df4)
ss2 = ss1[3:5]  # declaring Series with 2 last columns of Yahoo row
print(ss2)
df4 = df3 + ss2  # adds values to specified columns and turn other values NaN
print(df4)

# MORE MATH:
sales1 = pd.Series([200,300,400,500],index=['Yahoo','Facebook','Microsoft','Google'])
sales2 = pd.Series([150,250,350,450],index=['Yahoo','Facebook','Microsoft','Google'])
sales3 = pd.Series([100,200,300,400],index=['Yahoo','Facebook','Microsoft','Google'])
df1 = pd.DataFrame({2017:sales1,2016:sales2,2015:sales3})
print(df1)
sales4 = pd.Series([200,300,400,500],index=['Amazon','Ebay','Jumia','Etsy'])
sales5 = pd.Series([150,250,350,450],index=['Amazon','Ebay','Jumia','Etsy'])
sales6 = pd.Series([100,200,300,400],index=['Amazon','Ebay','Jumia','Etsy'])
df2 = pd.DataFrame({2017:sales4,2016:sales5,2015:sales6})
print(df2)

df3 = df1 + df2  # turn everyting NaN becouse not a single row is aligned
df3 = df1.append(df2)  # adds df2 rows to df1
print(df3)
df3 = df3[::2][[2016]]  # every second index for column '2016'
print(df3)
df3 = df1 + df3  # adds only aligned values of df3 to df1
print(df3)


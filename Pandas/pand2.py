import pandas as pd

# already know ht read from:
df1 = pd.read_csv("pandas-master/pokemon_data.csv")
dfxl1 = pd.read_excel("pandas-master/pokemon_data.xlsx")
# and also a txt file with specified delimiter (spacepoint):
dftx1 = pd.read_csv("pandas-master/pokemon_data.txt",delimiter='\t')

# print(df1.head(3))  # lines from the top of cvs
# print(dfxl1.tail(3))  # from the end of xlsl
# print(dftx1.head(5))  # or the top of txt
#
# # Read Dataframe Headers:
# print(df1.columns)
#
#
# # Read part
# print(df1.iloc[0:10,1:10])
# print(df1.loc[0:10,"Name":"Defense"])
#
# # Read each column:
# print(df1["Name"][0:5])  # (and rows); it may be also called
# # as a variable of a class:
# # print(df1.Name[0:5])
# print(df1[["Name", "HP", "Type 1"]][0:5])

# Read each row range of rows as slice
print(df1[0:9])

sdf1 = df1[0:13][["Name","Type 1","HP","Attack","Defense","Speed"]]

# it seems that order of giving args is not so important;
# pandas may take headers of col's first or numbers of
# rows as above, but for many strings "" we need a list []

# Read Specific Row displayed as a column:
print(sdf1.iloc[2])  # with dataframe class method 1th - row
# transposed as a column
# Read Specific Location coords [Row,Column]:
print(sdf1.iloc[2,0])
# Read Specific Location with Headers (not int):
print(sdf1.loc[0:3,["HP","Name"]])
# Even with conditions!:
print(sdf1.loc[sdf1["HP"] >= 70])

# Iterate through Rows:
lst = []
print("Start!")
for index, row, in sdf1.iterrows():
    if "Char" in row["Name"]:
        lst.append(row)
    else:
        print("Poke:\n", row)
print("Charmander forms:")
for i in lst:
    print(i)

# Math description of the data set:
print(sdf1.describe())

# Sorting:
print(sdf1.sort_values(["HP","Speed","Defense"], ascending=[0,1,0]))
# we can choose columns Headers and asc or desc order for each (sick!)


# SELECT 2 TYPES OF DATA
df1 = df1.loc[df1["Type 1"].str.contains("fire|grass", flags=re.I,regex=True)]
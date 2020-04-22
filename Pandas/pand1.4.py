import pandas as pd
# # PANDAS ELEMENTARY:
# # WORKING WITH REAL DATA: LOADING, SAVING
ib_df1 = pd.read_csv("realdata/4IB.F.csv")  # classic file loading
ib_df1.to_excel("realdata/4IB.F_1_4.xlsx")  # export to excel for future use
print("1. we use classic read:")
print(ib_df1)
# ib_df1 = ib_df1.set_index(["Date"])  # does the same as:
# 1:
ib_df1 = pd.read_csv("realdata/4IB.F.csv", index_col=0)  # but here we can just give
# positional index;
print("2. read with index_col=0, which uses first data col as index col header:")
print(ib_df1)
cols = list(ib_df1.columns.values)
cols1 =[]
for column in enumerate(cols):  # loop to make list with lowercase (for looping practice)
    i, col = column
    cols1.append(col.lower())
print(cols1)
date1 = ["date"]
cols2 = date1.append(cols1)
print(cols2)
# header=None for no header; header=int or list-like of ints
# to specify the row(s) making up the column names
# (in practice below no header means cols1 is added above present headers, and =0 deletes old row
ib_df1 = pd.read_csv("realdata/4IB.F.csv", names=cols1)  # here
# we use prepared lowercase list ['open', 'high', 'low', 'close', 'adj close', 'volume'] as a value
# for attribute names= and set header=0 to load the file immidiately with new cols names
print("3. read with names=list assigning new col's headers:")
print(ib_df1)
# ib_df1 = pd.read_csv("realdata/4IB.F.csv", names=cols1, index_col=1, header=0)
# print(ib_df1)  # returns same as above so
# WE CAN'T USE index_col= AND names= AT THE SAME TIME
ib_df1 = pd.read_csv("realdata/4IB.F.csv",
                     usecols=["Date","Open","Close"])  # and
# here we read only specified columns from the file; to make useless most of learned before xd
print("4. read with usecols=list which works as a slicing from the DF, "
      "NOT ADDING any headers:")
print(ib_df1)
ib_df1 = pd.read_csv("realdata/4IB.F.csv",
                     usecols=["Date","Open","Close"], index_col=0)
print("5. read with usecols=list and index_col=0 atst so it\n"
      "takes slice of list and establish 0th element as index header ")
print(ib_df1)
# 2:
# when saving file we may set name for index column with:
ib_df2 = pd.read_csv("realdata/4IB.F.csv", usecols=["Date","Open","Close"])
ib_df2.to_csv("realdata/4IB.F_temp.csv", index_label="#")  # adding the header
# for the unnamed index column makes it first (0) element of DF.columns.values list
# so then when we open it again we may put the "Date" column as an index:
ib_df3 = pd.read_csv("realdata/4IB.F_temp.csv", index_col=1)
print("6. We saved 5.DF with index_label='#' attribute and than we\n"
      "read it with index_col=1 atr which means it treat labeled index column as 0th position now:")
print(ib_df3)
ib_df3.to_excel("realdata/4IB.F_1_4_temp.xlsx")
ib_df3 = pd.read_excel("realdata/4IB.F_1_4_temp.xlsx")
# # IMPORTANT: remember that some file formats will automatically add positional indexing, and
# USING COLUMNS AS INDEXES IS ONLY POSSIBLE IN PANDAS and html(?):
# if we try to export xlsx to html it will have one more unnecessary index:
ib_df3.to_html("realdata/4IB.F_1_4final.html")


import pandas as pd
# import numpy as np
# # PANDAS ELEMENTARY:
# # SERIES: LOADING and SAVING data

# # SERIES:
# ss1 = pd.Series('a')
# ss2 = pd.Series(['a','b','c'])
# ss3 = pd.Series(['a','b','c'], index=[1,2,3])  # or
# ss3 = pd.Series({1:"a", 2:"b", 3:"c"})
# print(ss1)
# print(ss2)
# print(ss3)
#
# # RETURN DATA ABOUT series:
# serie1 = pd.Series([100,600,250,300,300,1000,np.nan])
# print(serie1)
# print(len(serie1),serie1.shape)  # length
# print(serie1.count())  # length for non-NaN val's
# print(serie1.unique())  # unique vals
# print(serie1.value_counts())  # with number of occurances, only non-Nan
#
# # RETURNING DATA VALUES from series:
# serie1 = pd.Series([100,600,250,300,300,1000,np.nan],
#                    index=["Mon","Tue","Wed","Thu","Friday","Sat","Sun"])
# print(serie1)
# print(serie1.index)  # return index list in tuple
# print(serie1.values)  # return values list
# print(serie1[["Mon","Wed"]], serie1[[0,2]])  # return chosen series
# print(serie1.take([0,2,5]))  # same but only with positional indexes
#
# # INDEXING RULES:
ss4 = pd.Series(['a','b','c','d'], index=[3,2,1,0])
print(ss4[1])  # if we use strings for indexing that [] notation returns the positional index
# # but if we use int's the default pos val's are overwritten
print(ss4[[1,2,3]])  # returns rows 1, 2 and 3
# print(ss4.loc[[1,3]])  # returns our index, but
# print(ss4.iloc[[1,3]])  # returns default pos index
# for indexing multiple rows in SERIES we may use [] notation:


#
# # ALIGNMENT, MATH ON SERIES:
# series1 = pd.Series([100,200,300,400],index=["A", "B", "C", "D"])
# series2 = pd.Series([10,20,30,40,50],index=["E","D","C","B","A"])
# print(series1)
# print(series2)
# print(series2 + series1)  # they are added according to our string index
# # not the def pos index; its ordered alphabetically
# # and not-aligned indexes return Nan
# series1 = pd.Series([100,200,300,400],index=["A", "A", "C", "D"])
# series2 = pd.Series([10,20,30,40],index=["D","C","A","A"])
# print(series1 + series2)  # returns 4 "A" values added each with each: x1+x1, x1+x2, x2+x1,x2+x2;
# # always in the index occurrences order not backwards, because it's default for index reading
# print(series1 * series2)
#
# # RE-INDEXING SERIES; .index .reindex(?) .astype():
# series3 = pd.Series([10,20,30,40,50])
# print(series3)
# series3.index = ["A", "B", "C", "D", "E"]  # changing default indexes
# print(series3)
# series4 = series3.reindex(["a","b","c","d","e"])
# print(series4)  # returns NaN's because new indexes are not the same as originals(?)
# series5 = pd.Series([10,20,30], index=[1,3,5])
# print(series5)
# series6 = pd.Series([10,30,30], index=["1","3","5"])
# print(series5 + series6)  # returns Nan's because indexes are non-aligned (different type)
# series6.index = series6.index.values.astype(int)  # converting types
# print(series5 + series6)  # now it may be computed

# SLICING SERIES:
# series1 = pd.Series([49,200,30,45],index=['john','smith','miller','jack'])
# print(series1[::-1])  # reversed slice

# # LOADING DATA:
#
# # from html it returns a list not a DataFrame structure
#
# # csv:
# csv_path = 'csv1.csv'
# df = pd.read_csv(csv_path)
#
# # xlsx:
# xlsx_path = 'excel1.xlsx'
# ex_df = pd.read_excel(xlsx_path)
#
# # from dict (keys- headers; values - lists as rows;
# songs = {"Album": ["Thriller","Back in Black", "The Dark Side of the Moon", "The bodyguard"],
#          "Artist": ["Michael Jackson","AC/DC","Pink Floyd","Withney Huston"],
#          "Released": [1982,1980,1973,1992],
#          'Length': [42,42,42,57]}
# songs_df = pd.DataFrame(songs)
# print("Our data frame:\n",songs_df)
#
# df_part = songs_df[["Album","Released","Length"]]
# print("Chosen part of data frame:\n",df_part)
#
# particular_item = songs_df.loc[3,"Artist"]
# print("Particular item from the data frame:\n",particular_item)
#
# df_slice = songs_df.iloc[2:2,0:3]
# print("Slice of data frame from chosen range:\n",df_slice)
#
# # SAVING DATA:
# lista2 = []
# dict2 = {}
# with open("wepCSV.csv","r+") as wep:
#     for line in wep.readlines():
#         line1 = line.replace(" ","")
#         lista2.append(line1)
#     print(lista2)
#     for line in lista2:
#         line1 = line.split(",")
#         dict2[line1[0]] = line1[1:6]
#     print(dict2)
# #
# # with open("wep1.csv","w") as wep1:
# #     for line in lista2:
# #         wep1.writelines(line)
# dict3 = {"weapon:": ["price:","dmg:","dmg type:","weight:","other:"]}
# dict3.update(dict2)
# weapons_df = pd.DataFrame(dict3)
# print(dict3)
# lista3 = ["weapon:","price:","dmg:","dmg type:","weight:","other:"]
# lista4 = []
# # lista4.append(lista3)
# for item in lista2:
#     a, b, c, d, e, *f = item.split(",")
#     e = e.replace("lb","")
#     e = int(e)
#     item1 = a, b, c, d, e, ",".join(f)
#     print(item1)
#     lista4.append(item1)
# print(lista4)
#
# weapons_df1 = pd.DataFrame(lista4)
# print(weapons_df1)
# # weapons_df.rename()
# transposed_df = weapons_df.transpose()
# print(transposed_df)
# weapons_df2 = transposed_df
# print(weapons_df2)
# print(weapons_df2[2].unique())
# weapons_df3 = pd.DataFrame(lista4)
# weapons_df3.columns = ["weapon:","price:","dmg:","dmg type:","weight:","other:"]
# print(weapons_df3)
# # weapons_df3["weight:"]>=3 - returns 'vector' of boolean values, and than
# # we can use it as an arg for weapons_df3 to make dataframe slice
# heavies_df = weapons_df3[weapons_df3["weight:"]>=4]
# print(heavies_df)
# # heavies_df.to_excel("heavies.xlsx")
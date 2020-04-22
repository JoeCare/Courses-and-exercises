import os, shutil
import openpyxl as xl

os.chdir('../')
os.getcwd()
shutil.copy('/home/morfina/Downloads/exc1.xlsx','/home/morfina/PycharmProjects/Project1/FilesHandling/Excel')
os.chdir('/home/morfina/PycharmProjects/Project1/FilesHandling/Excel')
# print(os.getcwd())
exc1wb = xl.load_workbook('exc1.xlsx', data_only=True)
ws = exc1wb["Arkusz3"]
col = ws["C"]
values1 = []
values2 = []
note = 0

for cell in col:
    if cell.value:
        values1.append(cell.value)
    if cell.value == 'bilans':
        ind = values1.index(cell.value)

print(f'{str(values1.pop(ind)).capitalize()} oficjalny do dnia ...: {sum(values1)}'
      f'\nW tym możliwych nierozliczonych godzin: {values1.count(-8)*-8}'
      f'')

values2 = ' '.join(map(str, values1))
#
# for cell in col:
#     values1.append(cell.value)
#
# for n in values1:
#     if values1.count(None) > 0:
#         ind = values1.index(None)
#         values1.pop(ind)
#     elif values1.count(-8) > 0:
#         values1.remove(-8)
#
# del values1[0]
# print(sum(values1))
#
#


# for n in values1:
#     if type(n) != None:
#         values2.append(n)
#
# print(values2)
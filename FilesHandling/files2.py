import os, re


# FILE SIZE
path2 = '/home/morfina/PycharmProjects/Project1/RegularExpressions/'
print('size:', os.path.getsize('/home/morfina/PycharmProjects/Project1/RegularExpressions/'))
print(os.path.getsize(path2))
# AND DIR CONTENT:
# dir1 = os.listdir(os.path.split('/home/morfina/PycharmProjects/Project1/RegularExpressions/regex1.py')[0])
# print(dir1)
dir2 = os.listdir('/home/morfina/PycharmProjects/Project1/RegularExpressions/')
print(dir2)
total = 0
files = ""
for file in dir2:
    regexFile = re.compile(r'.*\.\w{,4}').search(file)
    print(regexFile)
    # OMG I FINALLY MADE IT MATCH!!
    if regexFile:
        file = regexFile.group()
        print(f'{file}: {os.path.getsize(os.path.join(path2, file))} bytes')
        total += os.path.getsize(os.path.join(path2, file))

        files += file + ", "
print(f'Complete size of {files.rstrip(", ")}: {total} bytes.')
print('cwd:', os.getcwd())
# print(os.path.getsize(path1))

# exc1. open an xlsx file and using regex sum all the negative numbers from one of the columns

# excer = open('./Excel/example file2.py','w+')
# excer.close()
print(os.path.abspath('../../../Downloads'))
# >>> '/home/morfina/Downloads'  #there was few more guesses before I've got:
print(os.path.isabs('/home/morfina/Downloads'))
# >>> True
print(os.listdir('/home/morfina/Downloads'))
# >>> ['exc1.xlsx']  # so I've found my file!!

# with open('/home/morfina/Downloads/exc1.xlsx','r') as exc1:
#     exc1.readline(4)
    # >>> UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 10: invalid start byte
# and that would be all, cuz python doesnt recognize the file and we cant just open it here
# lets go to...

# files3 = open('./files3.py','w+')
# files3.close()



import os
import re


# print(os.getcwd())
# >>> current working directory path
# os.path.join('usr','bin')
# joins directories indicated in strings with correct formula (backslash for Win, forward slash for Unix)
# >>> usr/bin
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/home/morfina/PycharmProjects/Project1/FilesHandling/', filename))

# ABSOLUTE PATH:
# full path always started with root i.e C:\Program Files\Documents\Pythons\files.py
print(os.getcwd())
print(os.path.isabs('./'))
print(os.path.abspath('../'))


# RELATIVE PATH:
# accordingly to current working directory
print(os.path.relpath('/home/'))
# >>> ../../..
print(os.path.relpath('/regex1.py'))
# >>> ../../../../regex1.py
# A single period (“dot”) for a folder name is shorthand for “this directory.”
# Two periods (“dot-dot”) means “the parent folder.”
path1 = '/home/morfina/PycharmProjects/Project1/RegularExpressions/regex1.py'
print(os.path.dirname(path1))
# >>> gives a path to parent directory (everything before last slash)
print(os.path.basename(path1))
# >>> gives a name of last object in the path (everything after last slash)
# important: it does not mean that it names all the files in the indicated file directory
print(os.path.split(path1))
# >>> ('/home/morfina/PycharmProjects/Project1/FilesHandling', 'files1.py')
# splits dir name and base name returning them a tuple; as well as:
print((os.path.dirname(path1), os.path.basename(path1)))
print(path1.split(os.path.sep))
# >>> ['', 'home', 'morfina', 'PycharmProjects', 'Project1', 'FilesHandling', 'files1.py']
# returns list of all names in the path
print(os.sep)
print(os.getcwd())

# os.chdir('./FilesHandling')
# Changes cwd
# os.makedirs('./FilesHandling/Excel')
# Creates directories




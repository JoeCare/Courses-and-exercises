# CASE INSENSITIVE REGEX:
import re


def take_pattern(regex):
    mo = regex.search("hahaha")
    if mo:
        return mo.group()
    else:
        return False


rege1 = re.compile('Hahaha')
rege2 = re.compile('HAHAHA')
rege3 = re.compile('hAhAHa', re.I)
# flag re.I or re.IGNORECASE as 2nd arg match strings ignoring if letters are big or small

print(take_pattern(rege1), take_pattern(rege2), take_pattern(rege3))


# SUBSTITUTING TEXT:
# cellNum = "My cellphone numbr is: 506 789 891"
# print(findCellPhone(cellNum))
# subsRegex = re.sub(r'\d\d\d \d\d\d \d\d\d',r'(26)\d\d\d \d\d\d \d\d\d',cellNum)
# print(subsRegex)
# my trial 1th from a scratch

def substitution(text):
    pattern = re.compile(r'.\d\d\d?')
    subst = pattern.sub('(+26)',text)
    if subst:
        return subst
    else:
        return False

cellNum = "My cellphone numbr is: 506 789 891"
rege4 = re.compile(r'\d\d\d \d\d\d \d\d\d').search(cellNum)
print(rege4.group())
print(substitution(cellNum))

namesReg = re.compile(r'Agent (\w)\w*')
subReg = namesReg.sub(r'\1****', 'Agent Alice gave a gun to Agent Bob.')
print(subReg)
# thaaat is preety strange shit... substitution so changing sth to sth with dedicated .sub() method
# but here first we need to declare compiled regex 'Agent \w+' - which matches string:
# 'Agent, space, single string of one or more letters'; than on that regex we use method .sub()
# of which first argument is a string that replaces what above regex match and second is
# normal string to which we input the changes
regex = re.compile(r'insert \d\w+ \w+')
sub1 = regex.sub('|insertion|','Oryginal string where we insert 1th arg in place that matches regex.')
print(sub1)
sub2 = re.compile('.$').sub(' -',sub1)
print(sub2, re.compile('re.compile').sub('', str(regex).replace("(","").replace(")",".")))

namesReg = re.compile(r'(Agent) (\w)\w*')
subReg = namesReg.sub(r'\2 ****', 'Agent Alice gave a gun to Agent Bob.')
print(subReg)
# so the regex indicate chunk with Agent, space, letter as a regex group, letter zeroormore
# for which we look in 2nd arg of .sub() and replaces it with its 1th arg
# Agent string is somehow completely erased and
# after space we look for letter to match our group in bracket which is just single letter
# than we look for zeroormore letters in a row and its our whole regular expression until
# non-letter sign (like space); whole regex match should be replaced with .sub()'s 1th argument but in it
# we used \1 which indicates first group of matched expression itself (which normally would point just what
# to get rid of for sake of .sub's 1th) will be a part of substituting string
# by using () brackets to create group we distinguish that part of regex for further use



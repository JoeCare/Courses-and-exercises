import re



def findCellPhone(text):
    """Function takes string as an arg and check if it fits expression of the cell phone kind.
    Returns that number if occur or False if nothing fits regex."""
    regObject = re.compile(r'\d\d\d \d\d\d \d\d\d')
    out = regObject.search(text)
    if out:
        return out.group()
    else:
        return False
# msg = input("Give me Your phone number.")
# print(findCellPhone(msg))

# MORE GROUPING:

def findFullName(text):
    """Takes string and checks if it contains fullname in given format. Returns that fragment or false
    if nothing fits."""
    fullName = re.compile(r'[ABCDEFGHIJKLMNOPRTUWXYZ]\w+ [ABCDEFGHIJKLMNOPRTUWXYZ]\w+')
    mo = fullName.search(text)
    if mo:
        return mo.group()
    else:
        return False


# msg1 = input("Give me Your full name.")
# print(findFullName(msg1))

# GREEDY AND NON-GREEDY REGEX'es:

def findWord(text):
    word = re.compile(r'\w{2,}?')  # question mark at the end of regex match object indicate
    # that match'll be non-greedy (take shortest match)
    mo = word.search(text)
    if mo:
        return mo.group()
    else:
        return False


msg2 = "Little Dorothy is happy."  # input("Give me some words.")
print(findWord(msg2))

# NOTES:
print(type(re.compile(r'\d\d\d')))
print(re.compile(r'\d\d\d'))
# regular expression Pattern class

print(type((re.compile(r'\d\d\d')).search("ABCD1234")))
print((re.compile(r'\d\d\d')).search("ABCD1234"))
# regular expression Match class

print(type((re.compile(r'\d\d\d')).search("ABCD1234").group()))
print((re.compile(r'\d\d\d')).search("ABCD1234").group())
# regular expression grouped Match - string class

print((re.compile(r'\d*')).search("ABCD1234").group())
# * sign after character class means ZERO OR MORE occurances needed for match
print((re.compile(r'\d+')).search("ABCD1234").group())
# +
print((re.compile(r'[awC123]')).search("ABCD1234").group())

print((re.compile(r'[^\d]')).search("ABCD1234").group())
# ^ sign on the beggining of class character bracket [] is negation of that class
print((re.compile(r'^\w')).search("ABCD1234").group())
# ^ sign on the beggining of raw string of expression means the match must start with that character class
print((re.compile(r'\d$')).search("ABCD1234").group())
# $ sign on the end of the rstring of regex means searched expression must end with that character class
print((re.compile(r'^\w+$')).search('ABCD1234A').group())
# ^ on the beggining and $ on the end of pattern indicates that searched string
# has to begin and end with particular character class
print((re.compile(r'.\w.\d.')).search('ABCD1234A').group())
# . sign is a Joker In The Pack, it'll match any character class except newline
# so here it matches first letter (C) before which there is some character (B) as well as after it (D)
# then as a digit 1 is a match and 2 is another wildcard character


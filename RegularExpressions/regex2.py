# MATCH (almost) EVERYTHING:
import re


def match_all(text):
    """Function look for string with First Name: and matches with everything which after it to the
    newline sing and then Last Name: with everything further. It also grouping this two wild matches into
    two separate strings in tuple.
    """
    al = re.compile(r'First Name: (.*)\nLast Name: (.*)')
    mo = al.search(text)
    if mo:
        return mo.group(1,2)
    else:
        print(al, mo)
        return False


msg = "First Name: John\nLast Name: Doe"
print((match_all(msg)))
# .* signs matches with zero or more of whatever character class except newline so if newline would appear
# in above example i.e. after : whole expression wouldn't match and return None. .* works in greedy way;
# if we need non-greedy matching it should be:

nonGreedy = re.compile(r'<.*?>')
mo = nonGreedy.search("<Typing here> is more important > than here.")
print(mo.group())
# that regex pattern matches with string in which there is triangular
# bracket < with any characters classes in it > but it stops after
# first match of such a construct and ignore rest of the searched string
# so GREEDY regex tries to match longest possible string while
# NON-GREEDY matches shortest.

al1 = re.compile(r'First Name:(.*?)').search(msg)
print(al1, al1.group())
# trying non-greedy that way seems to be completely pointless
# cuz * 'zero or more' stops on zero as minimal matching length and takes nothing after : sign


# MATCH (really) EVERYTHING:
# re.DOTALL flag as second argument to the compile() method
def match_really_all(text):
    everythingRegex = re.compile(r'.*',re.DOTALL)
    mo1 = everythingRegex.search(text)
    if mo1:
        return mo1.group()
    else:
        return False


msg = "one2\n3four\nfivesix\n7\n"
print(match_really_all(msg))
# OR obviously shorter without function (but functions are good
# cuz once written we may use them later):
everythingRegex = re.compile(r'.*',re.DOTALL)
mo1 = everythingRegex.search("sy712t8\n217\nshk18Na")
print(mo1.group())

import re


phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneNum = phoneRegex.search("(222)-555 4321 ext.2345")
print(phoneNum.group())
pRegexVerbo = re.compile(r'''(
(\d{3}|\(\d{3}\))?            # area
(\s|-|\.)?                    # separator
\d{3}                         # 1th chunk
(\s|-|\.)                     # separator
\d{4}                         # 2nd chunk
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension 
)''',re.VERBOSE)

print(pRegexVerbo.search("(222)-555 4321 ext.2345").group())

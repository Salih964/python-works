#quantifiers (*,+,?,{})
from re import *

text="aabaaabcaabccaaaa"

#pattern="a*" #chk for any number of a including zero
#pattern="a{2}" #chk for 2a
pattern="a{2,3}" #chk for min 2 and max 3
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

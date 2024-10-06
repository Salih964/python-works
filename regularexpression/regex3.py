from re import *
text="abc K4gh$ 7dg"
#     0123456789
# lower case alphabets
# pattern="[a-z]" #chk for all lowercase alphabets
# pattern="[A-Z]" #chk for all upper case alphabets
# pattern="[a-zA-Z]" #chk for all alphabets
# pattern="[0-9]" #chk for all digits
# pattern="[a-zA-Z0-9]" #chk for alpha numeric characters
pattern="[^a-zA-Z0-9]" #chk for alpha numeric characters
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

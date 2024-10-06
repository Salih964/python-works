from re import *
text="fatboy@2k2#"

pattern="[abc]" #either a,b or c
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group()) #position match
from re import *

text="fatboy@2kB2#"
#pattern="\d" #[0-9] digits
#pattern="\D" #[^0-9] exclude digits
#pattern="\w" #[a-zA-z0-9] alpha numeric
pattern="\W" #[^a-zA-Z0-9] special characters

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())


#\s space
#\S exclude space

from re import fullmatch

month=""
rule="(0[1-9]|1[012])"

matcher=fullmatch(rule,month)
if(matcher!=None):
    print("valid")
else:
    print("invalid")    




from re import *
text="nUM1"

rule="[a-zA-Z][a-zA-Z0-9]*"

matcher=fullmatch(rule,text)

if(matcher==None):
    print("invalid")
else:
    print("valid")    
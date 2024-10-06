from re import fullmatch

date="30"
rule="(0[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(rule,date)
if(matcher==None):
    print("invalid")
else:
    print("valid")    

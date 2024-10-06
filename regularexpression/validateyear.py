from re import fullmatch

year="1800" #1800 2024

rule="((18|19)\d{2}|20[01]\d|202[0-4])"

matcher=fullmatch(rule,year)
if(matcher!=None):
    print("valid")
else:
    print("invalid")    


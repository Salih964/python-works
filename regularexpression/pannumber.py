from re import fullmatch

pancard="DTZZS6463J"
# first 3 char(Alphabets)
# 4th place P,C,A,F,H,T
# 5th place Alphabet
# followed by 4 digits
# alphabets in lastplace

rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(rule,pancard)
if(matcher!=None):
    print("valid")
else:
    print("invalid")    
from re import fullmatch

path="C:\\Users\\2\\OneDrive\Desktop\\mypython works\\regexpro\\pannums.txt"

f=open(path,"r",encoding="UTF-8")
rule="[A-Z]{3}[PCHAFT][A-Z]\d{4}[A-Z]"
for line in f:
    pan_number=line.rstrip("\n")
    matcher=fullmatch(rule, pan_number)
    if matcher != None:
        print(pan_number)
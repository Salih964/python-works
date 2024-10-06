from re import fullmatch

path="C:\\Users\\2\OneDrive\\Desktop\\mypython works\\regexpro\\tcodes.txt"

f=open(path,"r",encoding="UTF-8")

rule="\d{3}[/]\d{2}[/]R\d{2}[/]\d{2}[a-z]"

for line in f:
    code=line.rstrip("\n")
    matcher=fullmatch(rule, code)
    if matcher != None:
        print(code)
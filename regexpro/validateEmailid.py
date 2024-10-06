from re import fullmatch
path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\regexpro\\emailid.txt"
f=open(path,"r",encoding="UTF-8")
# starting with lower case alphabet
# followed by any number of alphabets number_-
rule="[a-z][0-9a-z_-]*@gmail.com"
for line in f:  
    Email_Id=line.rstrip("\n")
    matcher=fullmatch(rule,Email_Id)
    if matcher!= None:
       print(Email_Id)
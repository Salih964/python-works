from re import *

phone_number="+918386398719"

rule="(\+91)?[0-9]{10}"

matcher=fullmatch(rule,phone_number)

# if(matcher==None):
#     print("invalid")
# else:
#     print("valid")    

print("invalid" if matcher ==None else "valid")
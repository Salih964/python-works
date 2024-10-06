#kl-08-BN-4970
from re import *

regnum="KL08BN4970"
rule="(KL)\d{2}[A-Z]{1,2}\d{4}"
matcher=fullmatch(rule,regnum)

if(matcher==None):
    print("invalid")
else:
    print("valid")    
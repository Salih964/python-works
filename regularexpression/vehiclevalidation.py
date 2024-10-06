from re import fullmatch

vehicle_number="KL-08-BN-4970"

rule="(KL)[-]?\d{2}[-]?[A-Z]{1,2}[-]?\d{4}"

matcher=fullmatch(rule,vehicle_number)
if(matcher!=None):
    print("valid")
else:
    print("invalid")    

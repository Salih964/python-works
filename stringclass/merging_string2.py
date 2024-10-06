

string1=input("enter string")

string2=input("enter string2")

s1_length=len(string1)

s2_length=len(string2)

smallest_length=s1_length if s1_length < s2_length else s2_length

out=""

for i in range(0,smallest_length):
    out=out+string1[i]+string2[i]

if len(string1) > len(string2):
    rem=string1[smallest_length:] 
else:
    rem=string2[smallest_length:]    
out+=rem
print(out)      

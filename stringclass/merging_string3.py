string1=input("enter string")
string2=input("enter string2")

length=min(len(string1),len(string2))

result=""
for i in range (0,length):
    out=string1[i]+string2[i]
    result+=out

if len(string1)>len(string2):
    rem=string1[length:] 
else:
    rem=string2[length:]  

result+=rem
print(result)  
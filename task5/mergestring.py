string1="ABC"

string2="PQRST"

output=""
length=len(string1)

for i in range(0,length):
    output=output+string1[i]+string2[i]
    
rem=string2[length:]
output+=rem
print(output)
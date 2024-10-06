# string1="ABCD"
# string2="PQRST"
# out=APBQCRDT

string1="ABC"
#        123
string2="PQRST"
#        12345
output=""
length=len(string1)

for i in range(0,length):
    output=output+string1[i]+string2[i]
    
rem=string2[length:]
output+=rem
print(output)
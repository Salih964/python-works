text="LUMINAR"
    # 0123456 
# string slicing

print(text[2:5]) #MIN

# [string:stop:step]
print(text[2:5])
print(text[:5])
print(text[4:])
print(text[:])
print(text[-1:-4:-1])
print(text[::-1])

# length=len(text)-1
# result=""
# for i in range(length,-1,-1):
#    result=result+text[i]
# print(result)

reversed_string=text[::-1]
print(reversed_string)
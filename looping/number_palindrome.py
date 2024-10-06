# chk number is palindrome or not
# result=""
# num=121
# last_digit= num%10 
num=121
result="" #"121"
original=num
while(num!=0):
    digit=num%10
    result=result+str(digit)
    num=num//10
print(result) #type=str
if(original ==int(result)): #121==int("121")
  print("palindrome")
else:
   print("not palindrome")


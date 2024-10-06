num=int(input("enter number"))

# this method is used for checking only one number

# original=num
# result=""

# while(num!=0):
#    digit=num%10
#    result=result+str(digit)
#    num=num//10

# if int(result)==original:
#    print(result,"is palindrome")   
      

while(True):
    if num!=0:
      original=num
    else: 
       num=original
    result=""

    while(num!=0):
       digit=num%10
       result=result+str(digit)
       num=num//10

    if original==int(result):
       print(original,"palindromic number")
       break
    original+=1

# # #
def palindrome(num):
   while(True):
      if num !=0:
         original=num
      else:
         num=original
      result=""
      while(num!=0):
         digit=num%10
         result=result+str(digit)
         num=num//10
      if original==int(result):
         return (original)
      
      original+=1

if num==palindrome(num):    
   print(palindrome(num+1))
else:
   print(palindrome(num))   

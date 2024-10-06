def palindrome(num):
   
   reversed=str(num)[::-1]
   while str(num)!=reversed:
     num=num+1
   print(num)
palindrome(143)
# 1 to 100
# if num by / 3 abc
# if num /by 5 def
# if num /by 15 abcdef
# else num

i=1
while(i<=100):
    if i%15==0:
     print("abcdef")

    elif i%5==0:
     print("def")

    elif i%3==0:
      print("abc")
      
    else:
      print(i)
    i=i+1
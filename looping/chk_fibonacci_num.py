# chk wthr given nmber is exist in fibonacci series
num=22
is_fibo=False
prev=0
current=1

for i in range (1,num+1):

    next=prev+current
    prev=current
    current=next
    if next==num:
        is_fibo=True
        break 
      
print(is_fibo)
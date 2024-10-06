num1=int(input("enter num1"))
num2=int(input("enter num2"))

max_num=max(num1,num2)
while(True):
    if max_num%num1==0 and max_num%num2==0:
        lcm=max_num
        break
    max_num+=1
print(lcm)
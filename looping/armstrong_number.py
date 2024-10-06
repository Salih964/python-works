num=input("enter number") #153

digit_count=len(num)
num=int(num)#153
original=num
sum=0
while(num!=0): #153!=0
    digit=num%10 #153%10=3
    exp=digit**digit_count
    sum=sum+exp
    num=num//10 #num=153//10=15,num=1 num=0
    #num=0
print("armstrong" if original ==sum else "not armstrong")

#q1) num=153 out=5**3+4**3+3**3

# etract digit
# cube
# add with sum
# floor

#armstrong number
num=370
sum=0

while(num!=0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10
print(sum)    

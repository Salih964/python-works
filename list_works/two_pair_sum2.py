arr=[2,4,3,5,6]
sum=8
l=0
r=len(arr)-1
arr.sort()
is_present=False
while(l<r):
    l_element=arr[l]
    r_element=arr[r]
    current_sum=l_element+r_element
    if sum==current_sum:
        print("pairs",l_element,r_element)
        is_present=True
        break
    elif sum>current_sum:
        l=l+1
    elif sum<current_sum:
        r=r-1    
if is_present==False:
    print("no pair exist")
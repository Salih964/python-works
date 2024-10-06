arr=[5,1,4,2,3]
arr.sort()
left=0

while(left<len(arr)-1):
    right=left+1
    right_element=arr[right]
    left_element=arr[left]

    if right_element-left_element!=1:
        print(left_element+1,"is missing")
        break
    else:
        left=left+1
else:
    print(right_element+1,"is missing")        
       

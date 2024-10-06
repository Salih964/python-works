arr=[2,3,5,4]

print(len(arr))

sum=9
is_present=False
counter=0

for i in range (0,len(arr)-1):
    for j in range (i+1,len(arr)):
        i_element=arr[i]
        j_element=arr[j]
        current_sum=i_element+j_element
        if current_sum==sum:
            print("pairs",i_element,j_element)
            is_present=True
            break
        counter+=1
print("total number of execution",counter)

if is_present==False:
    print("no pair exist")
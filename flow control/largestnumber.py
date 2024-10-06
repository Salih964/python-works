# read three numbers num1,num2, and num3 find largest number using if, elif
# read three numbers num1,num2,and num3 find second largest number using if,elif
# read three numbers num1,num2,and num3 sort these three numbers using if,elif
 
# Read three numbers
num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))
num3 = int(input("Enter the number"))

# Find  largest number
if num1>num2 and num1>num3:
    print(f"largest number {num1}")
elif num2>num1 and num2>num3:
    print(F"largest number {num2}")
elif num3>num1 and num3>num2:
    print(f"largest number{num3}")

#  find second largest number
if (num1>num2) and (num1>num3):
    # first_num=num1
    if num2>num3:
         print(f"second largest number{num2}")#num1,num2,num3
    else:
        print(f"second largest number {num3}")#num1,num3,num2

elif(num2>num1)  and (num2>num3):
    # first_num=num2
    if num1 >num3:
     print(f"second largest number{num1}")#num2,num1,num3  
    else:
        print(f"second largest number {num3}")#num2,num3,num1

elif(num3>num1) and (num3>num2):
    # first_num=num3
    if num1>num2:
        print(F"second largest number{num1}")#num3,num1,num2
    else:
        print(f"second largest number {num2}")#num3,num2,num1

# sorting of num1,num2,num3
if (num3>num1) and (num3>num2):
    if num3>num1:
      print(f"third argest number{num1}")
    else:
     print(f"third largest number{num2}")

elif(num2>num1) and (num2>num3):
    if(num2>num1):
        print(f"third largest number{num1}")
    else:
         print(f"third largest number {num3}")

elif (num1>num2) and (num1>num3):
    if(num1>num2):
     print(f"thid largest number{num2}")
    else:
        print(f"third largest number{num3}")

# using chat gpt  for Sorting the numbers using if and elif
if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Displaying the sorted numbers
print(f"Sorted numbers: {smallest}, {middle}, {largest}")

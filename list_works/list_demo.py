expenses=[15000,20000,16000,17000,12000]

# print(expenses[1])

# # update 
# expenses[2]=18000
# print(expenses)

# for i in range(0,len(expenses)):
#     print(expenses[i])

# for obj in expenses:
#     print(obj)

# print  all expenses >19000
# for obj in expenses:
#     if obj>19000:
#       print(obj) 

# print all expenses in range of 15k -18k   
# for obj in expenses:
#     if obj in range(15000,18001):
#        print(obj)

    #or you can use this method
    # if obj>=15000 and obj<=18000:
    #    print(obj)
    
#  total sum
total=sum(expenses)
print(total)
# costly expenses
print(max(expenses))
# cheapest expense     
print(min(expenses))
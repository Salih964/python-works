list=[1,2,3,4,5,7]
#without condition#
# squares
squares=[num**2 for num in list]
print(squares)

# cube
cubes=[num**3 for num in list]
print(cubes)

# add
add_five=[num+5 for num in list]
print(add_five)

#with condition#
#even
evens=[num for num in list if num%2==0]
print(evens)

#odd
odds=[num for num in list if num%2!=0]
print(odds)

# new list
languages=["python","c++","c","java","java script","typescript"]

new_list=[]

for lang in languages:
    new_list.append(lang.upper())
print(new_list)

# new list using smaller step
new_list=[lang.upper() for lang in languages]
print(new_list)

# filter names count>5
len_filter=[lang for lang in languages if len(lang)>5]
print(len_filter)

# maped nums
list=[2,4,6,3,1]
maped_nums=[num+1 if num>5 else num-1 for num in list]
print(maped_nums)

# 0,1
lst=["-","+","-","-","+","-","+","+"]
map_symbols=[ 1 if sym=="+" else 0 for sym in lst]
print(map_symbols)
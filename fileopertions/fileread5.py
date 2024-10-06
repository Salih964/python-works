path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\orders.txt"
f=open(path,"r")
items=[]

for line in f:
    data=line.strip("\n")
    items.append(data)
print(set(items)) 

wc={i:items.count(i) for i in set (items)}
print(wc)

value_key=[(v,k) for k,v in wc .items()]
print(max(value_key))

print(sorted(value_key,reverse=True))
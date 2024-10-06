path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\worldcup.txt"

f=open(path,"r")

teams=[]

for line in f:
    data=line.rstrip("\n").split(" ")
    teams.append(data[1])

# print(teams)
# winners
print(set(teams))

wc={t:teams.count(t) for t in set (teams)}

value_key_list=[(v,k) for k,v in wc.items()]
print(max(value_key_list))
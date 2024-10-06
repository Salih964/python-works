
path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\colors.txt"

f=open(path,"r")
colors_list=[]
for line in f:
    colors_list.append(line.rstrip("\n"))
print(set(colors_list))
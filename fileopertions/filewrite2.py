list=["red","green","blue","white"]
path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\colors.txt"
f=open(path,"w")
for c in list:
    f.write(c+"\n")

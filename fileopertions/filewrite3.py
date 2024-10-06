vehicle_numbers=["KL-03-AC-1279","TN-4-DB-3456","AN-06-AM-2345","KL-04-AN-4567","KA-23-ER-2314"]

path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\vehiclnum.txt"

f=open(path,"w")
for num in vehicle_numbers:
    if num.startswith("KL"):
        f.write(num+"\n")

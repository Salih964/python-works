path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\story.txt"

f=open(path,"r")
all_words=[]

for line in f:
    cleaned_string=line.strip("\n")
    words=cleaned_string.split(" ")
    for w in words:
        all_words.append(w)
print(all_words)
wc={w:all_words.count(w)for w in set(all_words)}
print(wc)
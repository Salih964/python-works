text="goodmorning"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for k,v in wc.items():
    if v>1:
        print(k)

# count
set_text=set(text)
wc={}
for ch in set_text:
    wc[ch]=text.count(ch)
print(wc)
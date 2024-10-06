text="pnEumonoultramicroscopi@#c$silicovolcanoconiosis"
vowels=("a","e","i","o","u")
v_count=0
c_count=0

char_count=0

for ch in text:
  if ch.isalpha():
    char_count+=1

for ch in text:
  if ch.casefold() in vowels:
    v_count+=1
  else:
    c_count+=1  
print("v_count",v_count)
print("c_count",c_count)
print("char count",char_count)


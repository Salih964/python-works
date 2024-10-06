def count_vowels(txt):
    text=txt.casefold()
    count=0
    vowels=("a","e","i","o","u","A","E","I","O","U")
    for ch in txt:
        if ch in vowels:
            count=count+1
    return count  

txt="the quick brown for jumps over the lazy dog."
    
print(count_vowels(txt)) 
source_word="listen"
target_word="silent"

srt_source_word=sorted(source_word)
srt_word=sorted(target_word)

if srt_source_word==srt_word:
    print("anagram")
else:
    print("not anagram")    

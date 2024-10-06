# q1
word="ammma"
#     123456789=> length count
#     012345678=> index count means (input values in square bracket)

result=""
for i in range (4,-1,-1):
    result=result+word[i]
    
print(result)

print("palindrome" if result==word else"not palindrome") 

# q2
word="malayalam"
length=len(word)-1
result=""

for i in range(length,-1,-1):
    result=result+word[i]
print(result)

# q3 print longest word in string and shortest word in string

text="this is a goodmorning msg"
words=text.split()

# max_word
def get_len(w):
    return len(w)
max_word=max(words,key=get_len)
print(max_word)

# min_word
def get_len(w):
    return len(w)
min_word=min(words,key=get_len)
print(min_word)

srt_words=sorted(words,key=get_len,reverse=True)
print(srt_words)
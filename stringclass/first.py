tweets=" this is a sampletweet @stock @sachi @salih mentioned"

# step1 extract words
words=tweets.split(" ")
print(words)

for w in words:
    if w.startswith("@"):
        print(w)
    
text="#orange color wow #yellow color wow #blue color wow"

words=text.split(" ")
for w in words:
    if w.startswith("#"):
        print(w.lstrip("#"))

text="i have 3 bikes 2 car"
# print numbers
words=text.split(" ")

for w in words:
    if w.isdigit():
        print(w)
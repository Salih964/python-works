numbers=[5,6,7,8,10,11,15]

odds=list(filter(lambda num: num%2 !=0,numbers))

names=["python","pytz","django","rest","angular","pytorch"]

name_filter=list(filter(lambda w:w.startswith("py"),names))
print(name_filter)
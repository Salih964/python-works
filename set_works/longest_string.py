list=[10,20,20,40,50,20]

st=set(list)
print(st)

all_users={"sachin","dravid","laxman","jadeja","dhoni","raina"}

dhoni_friends={"sachin","raina"}

suggestion_set=all_users.difference(dhoni_friends)

suggestion_set.discard("dhoni")

print(suggestion_set)
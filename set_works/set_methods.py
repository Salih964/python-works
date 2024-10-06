st={10,20,30,40,"hello"}

# add
st.add(50)
print(st)

# pop()
st.pop()
print(st)

# remove
st.remove(40)
print(st)

# discard
st.discard(400)
print(st)

# union(),intersection(),difference()
st1={10,20,30,40}
st2={30,40,50,60}

# union
union_set=st1.union(st2)
print(union_set)

# intersection
intersection_set=st1.intersection(st2)
print(intersection_set)

# difference()
difference_set=st1.difference(st2)
print(difference_set)

# update
colors={"red","green","blue"}
new_set={"cyan","purple","brown"}
colors.update(new_set)
print(colors)
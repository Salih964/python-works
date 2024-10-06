course={"name":"django","language":"python","duration":7,"fees":50000,"faculty":"shyam"}

# keys(),values(),items(),get(),update(),pop(key)

# keys()

for k in course.keys():
    print(k)

# values
for v in course.values():
    print(v)

# items() => k,v
for k,v in course.items():
    print(k,v)   

# get(keys)=> value if the value is not there it print none
print(course.get("names")) 

# print(course("am here"))
print("am here")

# print(course.get("fees"))
print(course.get("fees"))

# update()
course.update({"duration":8,"fees":6000})
print(course)

# pop(key)
course.pop("faculty")
print(course)